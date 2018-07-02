from flask import current_app
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime

def encrypt_password(plaintext_password):
    """
    Hash a plaintext string using PBKDF2.

    :param plaintext_password: Password in plain text
    :type plaintext_password: str
    :return: str
    """
    if plaintext_password:
        return generate_password_hash(plaintext_password)

    return None



def encode_auth_token(self, user_id):
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



def hashPassword_sha1(password):
    import hashlib
    sha = hashlib.sha1()
    sha.update(password.encode('utf-8'))
    return sha.hexdigest()


# def hashPassword_bcrypt(password):
#     import bcrypt
#     return bcrypt.generate_password_hash(
#         password, current_app.config.get('BCRYPT_LOG_ROUNDS')
#     ).decode()    