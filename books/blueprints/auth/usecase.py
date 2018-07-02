from . utils import encrypt_password
from . repository import UserRepository
from . models import User
from ...utils.exceptionz import UserAlreadyExistsException
# from books.app import db
from books.blueprints.profile.models import UserProfile
from books.blueprints.profile.repository import UserProfileRepository

class RegisterUserUseCase():
    """
    
    """
    def __init__(self, repo=None, profile_repo=None):
        self.repo = repo or UserRepository()
        self.profile_repo = profile_repo or UserProfileRepository()

    def set_params(self, email, username, password, password2):
        self.email = email
        self.username = username
        self.password = password
        self.password2 = password2


    def execute(self):
        try:
            print('create user execute called {}')
            # email validation
            # compare password
            user = self.repo.get_user_by_email(self.email)
            # print('user-is {}'.format(user.email))
            if user:
                print('user-exists {}'.format(user.email))
                raise UserAlreadyExistsException(self.email)
                
            else:
                print('new-user')
                new_user = User(self.email, encrypt_password(self.password))
                print('new user-is {}'.format(self.username))

                self.repo.create_user(new_user)
                print('new-user-id {}'.format(new_user.id))

                user_profile = UserProfile(self.username, new_user.id)
                print('new-profile-is {}'.format(user_profile.name))
                self.profile_repo.create_profile(user_profile)
                
                from .tasks import send_confirmation_email
                send_confirmation_email.delay(new_user.email)

                return new_user
        except Exception as e:
            print(e)
        


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




