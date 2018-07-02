from . models import User
from books.app import db

class UserRepository():
    
    def get_all(self):
        return User.query.all()

    def get_user_by_email(self, email):
        return User.query.filter_by(email=email).first()

    def create_user(self, user):   
        print('repo creating user')  
        try:
            db.session.add(user)
            db.session.commit()  
            print('user added')      
            
        except Exception as e:
            print('error creating user {}'.format(e))
            db.session.rollback

