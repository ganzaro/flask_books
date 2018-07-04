import datetime
import bcrypt

from werkzeug.security import generate_password_hash, check_password_hash

def hash_pw_bcrypt(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def hash_pw_pbkdf2(plaintext_password):
    """
    Hash a plaintext string using PBKDF2.

    :param plaintext_password: Password in plain text
    :type plaintext_password: str
    :return: str
    """
    if plaintext_password:
        return generate_password_hash(plaintext_password)

    return None


# def hash_pw_sha1(password):
#     import hashlib
#     sha = hashlib.sha1()
#     sha.update(password.encode('utf-8'))
#     return sha.hexdigest()


# def hashPassword_bcrypt(password):
#     from flask_bcrypt import Bcrypt
#     return Bcrypt.generate_password_hash(
#         password, current_app.config.get('BCRYPT_LOG_ROUNDS').decode('utf-8'))

# bc.hashpw(pwd.encode('utf-8'), bc.gensalt())



