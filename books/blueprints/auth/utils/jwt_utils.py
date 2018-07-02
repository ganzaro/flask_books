import jwt
import datetime

from flask import current_app

def encode_auth_token(user_id):
    """
    Generates the Auth Token
    :return: string
    """
    try:
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=5),
            'iat': datetime.datetime.utcnow(),
            'sub': user_id
        }
        return jwt.encode(
            payload,
            current_app.config.get('SECRET_KEY'),
            algorithm='HS256'
        )
    except Exception as e:
        return e    





# from config import SECRET_KEY, JWT_ALGORITHM, TOKEN_EXPIRATION_SECONDS

# JWT_TIMESTAMP_KEY = 'timestamp'
# JWT_USER_ROLE = 'role'
# JWT_IDENTITY_KEY = 'identity'


# def create_jwt_token(user):
#     timestamp = datetime.datetime.now().timestamp() + TOKEN_EXPIRATION_SECONDS
#     jwt_object = {JWT_IDENTITY_KEY: user.username, JWT_TIMESTAMP_KEY: timestamp, JWT_USER_ROLE: user.role}
#     jwt_token = jwt.encode(jwt_object, SECRET_KEY, algorithm=JWT_ALGORITHM).decode('utf-8')
#     return jwt_token


# def parse_jwt_token(jwt_token):
#     jwt_contents = jwt.decode(jwt_token, SECRET_KEY, algorithm=JWT_ALGORITHM)
#     username = jwt_contents[JWT_IDENTITY_KEY]
#     timestamp = jwt_contents[JWT_TIMESTAMP_KEY]
#     role =  jwt_contents[JWT_USER_ROLE]
#     return username, timestamp, role
