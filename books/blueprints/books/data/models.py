import datetime as dt

from books.app import db


book_author_relation = db.Table('book_author',
    db.Column('book_id', db.Integer, db.ForeignKey('books.id')),
    db.Column('author_id', db.Integer, db.ForeignKey('authors.id'))
)


# user_loan_relation = db.Table('user_loan',
#     db.Column('user_profile_id', db.Integer, db.ForeignKey('user_profiles.id')),
#     db.Column('loan_id', db.Integer, db.ForeignKey('loans.id'))
# )

class Publisher(db.Model):

    __tablename__ = 'publishers'

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(60), index=True)
    address = db.Column(db.String(60))
    city = db.Column(db.String(60))
    country = db.Column(db.String(60))
    website = db.Column(db.String(255))

    # def __init__(self, **kwargs):
    #     db.Model.__init__(self, **kwargs)

    def __init__(self, name, **kwargs):
        db.Model.__init__(self, name=name, **kwargs)
    # def __repr__(self):
    #     return self.name

    def __repr__(self):
        return '<Publisher {}>'.format(self.name)  


class Author(db.Model):

    __tablename__ = 'authors'

    id = db.Column(db.Integer, primary_key=True)

    email = db.Column(db.String(255), index=True, unique=True, nullable=False)
    first_name = db.Column(db.String(60), index=True, nullable=False)
    last_name = db.Column(db.String(60), index=True, nullable=False)

    def __init__(self, last_name, **kwargs):
        db.Model.__init__(self, last_name=last_name, **kwargs)

    def __repr__(self):
        return self.last_name


class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(100), index=True)
    publication_date = db.Column(db.DateTime, nullable=False)

    publisher_id = db.Column(db.Integer,db.ForeignKey('publishers.id'))
    authors = db.relationship('Author', secondary=book_author_relation)
    # authors = db.relationship('Author', secondary=book_author_relation, backref=db.backref('books', lazy='dynamic'))

    # author_books = db.relationship('Author', backref='book', lazy='dynamic')


    # loans = db.relationship('Loan', secondary=user_loan_relation, backref=db.backref('subscribers', lazy='dynamic'))

    def __init__(self, title):
        db.Model.__init__(self, title=title)

    def __repr__(self):
        return self.title



