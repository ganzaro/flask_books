from . repository import PublisherRepository
from books.app import db
from ...utils.exceptionz import PublisherNotFoundException

class GetPublishersUseCase():

    def __init__(self, repo=None):
        self.repo = repo or PublisherRepository()

    def execute(self):
        return self.repo.get_all()


class GetPublisherUseCase():

    def __init__(self, repo=None):
        self.repo = repo or PublisherRepository()

    def set_params(self, id):
        self.id = id

    def execute(self):
        publisher = self.repo.get_one(self.id)
        if not publisher:
            raise PublisherNotFoundException(self.id)
        else:
            return publisher


class AddPublisherUseCase():

    def __init__(self, repo=None):
        self.repo = repo or PublisherRepository()

    def set_params(self, publisher):
        self.publisher = publisher

    def execute(self):
        self.repo.add_one(self.publisher)







