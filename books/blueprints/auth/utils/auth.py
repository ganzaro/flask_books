from werkzeug.security import generate_password_hash, check_password_hash
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