from . models import Publisher
from books.app import db


class PublisherRepository():
    
    def get_all(self):
        return Publisher.query.all()

    def get_one(self, id):
        return Publisher.query.filter_by(id=id).first()

    def add_one(self, publisher):
        db.session.add(publisher)
        db.session.commit()     