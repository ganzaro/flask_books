from . models import Publisher


class PublisherRepository():
    
    def get_all(self):
        return Publisher.query.all()

    def get_one(self, id):
        return Publisher.query.filter_by(id=id).first()

