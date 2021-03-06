# project/server/auth/views.py

import bcrypt
from flask import Blueprint, request, make_response, jsonify, abort
from flask.views import MethodView

from books.app import db
from books.blueprints.auth.data.models import User, BlacklistToken
from books.blueprints.profile.data.models import UserProfile
from .. import auth
from ..utils.jwt_utils import encode_auth_token
from .. usecase import GetUsersUseCase, \
            GetUserUseCase, RegisterUserUseCase
from ....libs.exceptionz import UserAlreadyExistsException
# TODO - 
# convert below to use usecase pattern


class RegisterAPI(MethodView):
    """
    User Registration Resource
    """
    def __init__(self, 
                get_user_uc=None,
                create_user_uc=None):

        self.get_user_uc = get_user_uc or GetUserUseCase()
        self.create_user_uc = create_user_uc or RegisterUserUseCase()
    
    def post(self):
        try:
            post_data = request.get_json()
            self.create_user_uc.set_params(
                post_data.get('email'),
                post_data.get('username'),
                post_data.get('password'),
                post_data.get('password2'))

            user = self.create_user_uc.execute()
            print('api-user-is {}'.format(user.email))

            # generate the auth token
            auth_token = encode_auth_token(user.id)
            resp = {
                'status': 'success',
                'message': 'Successfully registered.',
                'auth_token': auth_token.decode()
            }
            return make_response(jsonify(resp)), 201

        except UserAlreadyExistsException as e:
            resp = {
                'status': 'fail',
                'e': '{}'.format(e),
                'message': 'Some error occurred. Please try again.'
            }
            return make_response(jsonify(resp)), 401            

        except Exception as e:
            db.session.rollback()
            resp = {
                'status': 'fail',
                'e': '{}'.format(e),
                'message': 'Some error occurred. Please try again.'
            }
            return make_response(jsonify(resp)), 401

class LoginAPI(MethodView):
    """
    User Login Resource
    """
    def post(self):
        # get the post data
        post_data = request.get_json()
        try:
            # fetch the user data
            user = User.query.filter_by(
                email=post_data.get('email')
            ).first()
            # if user and bcrypt.check_password_hash(
            if user and bcrypt.checkpw(post_data.get('password').encode('utf-8'), user.password):

                # generate token
                auth_token = encode_auth_token(user.id)
                if auth_token:
                    responseObject = {
                        'status': 'success',
                        'message': 'Successfully logged in.',
                        'auth_token': auth_token.decode()
                    }
                    return make_response(jsonify(responseObject)), 200
            
            else:
                responseObject = {
                    'status': 'fail',
                    'message': 'User does not exist.'
                }
                return make_response(jsonify(responseObject)), 404
        except Exception as e:
            print(e)
            responseObject = {
                'status': 'fail',
                'message': 'Try again'
            }
            return make_response(jsonify(responseObject)), 500


class UserAPI(MethodView):
    """
    User Resource
    """
    def get(self):
        # get the auth token
        auth_header = request.headers.get('Authorization')
        if auth_header:
            try:
                auth_token = auth_header.split(" ")[1]
            except IndexError:
                responseObject = {
                    'status': 'fail',
                    'message': 'Bearer token malformed.'
                }
                return make_response(jsonify(responseObject)), 401
        else:
            auth_token = ''
        if auth_token:
            resp = User.decode_auth_token(auth_token)
            if not isinstance(resp, str):
                user = User.query.filter_by(id=resp).first()
                responseObject = {
                    'status': 'success',
                    'data': {
                        'user_id': user.id,
                        'email': user.email,
                        'admin': user.admin,
                        'registered_on': user.registered_on
                    }
                }
                return make_response(jsonify(responseObject)), 200
            responseObject = {
                'status': 'fail',
                'message': resp
            }
            return make_response(jsonify(responseObject)), 401
        else:
            responseObject = {
                'status': 'fail',
                'message': 'Provide a valid auth token.'
            }
            return make_response(jsonify(responseObject)), 401


class LogoutAPI(MethodView):
    """
    Logout Resource
    """
    def post(self):
        # get auth token
        auth_header = request.headers.get('Authorization')
        if auth_header:
            auth_token = auth_header.split(" ")[1]
        else:
            auth_token = ''
        if auth_token:
            resp = User.decode_auth_token(auth_token)
            if not isinstance(resp, str):
                # mark the token as blacklisted
                blacklist_token = BlacklistToken(token=auth_token)
                try:
                    # insert the token
                    db.session.add(blacklist_token)
                    db.session.commit()
                    responseObject = {
                        'status': 'success',
                        'message': 'Successfully logged out.'
                    }
                    return make_response(jsonify(responseObject)), 200
                except Exception as e:
                    responseObject = {
                        'status': 'fail',
                        'message': e
                    }
                    return make_response(jsonify(responseObject)), 200
            else:
                responseObject = {
                    'status': 'fail',
                    'message': resp
                }
                return make_response(jsonify(responseObject)), 401
        else:
            responseObject = {
                'status': 'fail',
                'message': 'Provide a valid auth token.'
            }
            return make_response(jsonify(responseObject)), 403


@auth.route('/auth/forgot-password', methods=['POST'])
def forgot_password():
    email = request.json.get('email')
    if email is None:
        abort(400)

    try:
        from ..tasks.tasks import deliver_password_reset_email

        deliver_password_reset_email.delay(email)
        # u = User.initialize_password_reset(email)
        msg = ('An email has been sent to {0}.'.format(email))

    except Exception as e:
        return jsonify({'message': e.__str__()}), 500
    
    return jsonify(msg), 200



# define the API resources
registration_view = RegisterAPI.as_view('register_api')
login_view = LoginAPI.as_view('login_api')
user_view = UserAPI.as_view('user_api')
logout_view = LogoutAPI.as_view('logout_api')

# add Rules for API Endpoints
auth.add_url_rule(
    '/auth/register',
    view_func=registration_view,
    methods=['POST']
)
auth.add_url_rule(
    '/auth/login',
    view_func=login_view,
    methods=['POST']
)
auth.add_url_rule(
    '/auth/status',
    view_func=user_view,
    methods=['GET']
)
auth.add_url_rule(
    '/auth/logout',
    view_func=logout_view,
    methods=['POST']
)
