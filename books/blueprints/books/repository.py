from . models import Publisher


class PublisherRepository():
    
    def get_all(self):
        return Publisher.query.all()



