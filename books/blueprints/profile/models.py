import datetime as dt

from books.app import db


class UserProfile(db.Model):

    __tablename__ = 'user_profiles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60))

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    user = db.relationship('User', backref=db.backref('profile', uselist=False))

    # loans = db.relationship('Loan', secondary=user_loan_relation, backref=db.backref('subscribers', lazy='dynamic'))

    def __repr__(self):
        return '<Profile %r>' % self.name

    def __init__(self, username, user_id):
        self.name = username
        self.user_id = user_id