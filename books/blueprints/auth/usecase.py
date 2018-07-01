from . utils import encrypt_password
from . repository import UserRepository
from ...utils.exceptionz import UserAlreadyExistsException
from books.app import db

class GetUsersUseCase():

    def __init__(self, repo=None):
        self.repo = repo or UserRepository()

    def execute(self):
        return self.repo.get_all()


class GetUserUseCase():

    def __init__(self, repo=None):
        self.repo = repo or UserRepository()

    def set_params(self, id):
        self.id = id

    def execute(self):
        return self.repo.get_user_by_email(self.id)


class RegisterUserUseCase():
    """
    TODO - 
    email validation
    compare password
    check if user exists, 
    create user
    create profile
    generate token
    send confirmation email

    --
    rollback if error
    """

    def __init__(self, repo=None):
        self.repo = repo or UserRepository()

    def set_params(self, username, password):
        self.username = username
        self.password = password


    def execute(self):
        user = self.repo.get_user_by_email(self.username)
        if user:
            raise UserAlreadyExistsException(self.username)
        else:
            return self.repo.create_user(self.username, encrypt_password(self.password))






