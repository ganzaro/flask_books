from . models import UserProfile
from books.app import db

class UserProfileRepository():
    
    def get_all(self):
        return UserProfile.query.all()

    def get_profile_by_username(self, email):
        return UserProfile.query.filter_by(email=email).first()

    def create_profile(self, profile):
        try:
            db.session.add(profile)
            db.session.commit()        
            
        except Exception as e:
            db.session.rollback
            print(e)


    