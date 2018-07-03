
import jwt
import datetime
from collections import OrderedDict

from flask import current_app
from itsdangerous import URLSafeTimedSerializer, \
    TimedJSONWebSignatureSerializer

from books.app import db, bcrypt
from .... libs.db_libs import AwareDateTime, ResourceMixin

# TODO - clean out models, move fns to repos, utils, etc...

class User(db.Model, ResourceMixin):
    """ User Model for storing user related details """

    ROLE = OrderedDict([
        ('member', 'Member'),
        ('admin', 'Admin')
    ])  

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    first_name = db.Column(db.String(60), index=True)
    last_name = db.Column(db.String(60), index=True)
    password = db.Column(db.String(255), nullable=False)
    phone_number = db.Column(db.String(12), index=True)

    is_admin = db.Column(db.Boolean, default=False)

    role = db.Column(db.Enum(*ROLE, name='role_types', native_enum=False),
                     index=True, nullable=False)
    
    active = db.Column('is_active', db.Boolean(), nullable=False,
                       server_default='1')

    # Email confirmation after register
    email_confirmed = db.Column(db.Boolean, nullable=True, default=False)
    email_confirmation_sent_on = db.Column(AwareDateTime(), nullable=True)
    email_confirmed_on = db.Column(AwareDateTime(), nullable=True)


    # Activity tracking.
    sign_in_count = db.Column(db.Integer, nullable=False, default=0)
    current_sign_in_on = db.Column(AwareDateTime())
    current_sign_in_ip = db.Column(db.String(45))
    last_sign_in_on = db.Column(AwareDateTime())
    last_sign_in_ip = db.Column(db.String(45))

    def __init__(self, email, password, **kwargs):
        super(User, self).__init__(**kwargs)
        self.email = email
        self.password = password


    @staticmethod
    def decode_auth_token(auth_token):
        """
        Validates the auth token
        :param auth_token:
        :return: integer|string
        """
        try:
            payload = jwt.decode(auth_token, current_app.config.get('SECRET_KEY'))
            is_blacklisted_token = BlacklistToken.check_blacklist(auth_token)
            if is_blacklisted_token:
                return 'Token blacklisted. Please log in again.'
            else:
                return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'

    @classmethod
    def initialize_password_reset(cls, identity):
        """
        Generate a token to reset the password for a specific user.

        :param identity: User e-mail address or username
        :type identity: str
        :return: User instance
        """
        # u = User.find_by_identity(identity).first()
        u = User.query.filter_by(email=identity).first()
        print('user {}'.format(identity))
        reset_token = u.serialize_token()

        # This prevents circular imports.
        from books.blueprints.auth.tasks import deliver_password_reset_email

        deliver_password_reset_email.delay(u.id, reset_token)
        print('********************************************************')
        print('model password_reset')
        return u


    @classmethod
    def find_by_identity(cls, identity):
        """
        Find a user by their e-mail or username.

        :param identity: Email or username
        :type identity: str
        :return: User instance
        """
        return User.query.filter(User.email == identity)
          #| (User.username == identity)).first()


    def serialize_token(self, expiration=3600):
        """
        Sign and create a token that can be used for things such as resetting
        a password or other tasks that involve a one off token.

        :param expiration: Seconds until it expires, defaults to 1 hour
        :type expiration: int
        :return: JSON
        """
        private_key = current_app.config['SECRET_KEY']

        serializer = TimedJSONWebSignatureSerializer(private_key, expiration)
        return serializer.dumps({'user_email': self.email}).decode('utf-8')


class BlacklistToken(db.Model):
    """
    Token Model for storing JWT tokens
    """
    __tablename__ = 'blacklist_tokens'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    token = db.Column(db.String(500), unique=True, nullable=False)
    blacklisted_on = db.Column(db.DateTime, nullable=False)

    def __init__(self, token):
        self.token = token
        self.blacklisted_on = datetime.datetime.now()

    def __repr__(self):
        return '<id: token: {}'.format(self.token)

    @staticmethod
    def check_blacklist(auth_token):
        # check whether auth token has been blacklisted
        res = BlacklistToken.query.filter_by(token=str(auth_token)).first()
        if res:
            return True
        else:
            return False
