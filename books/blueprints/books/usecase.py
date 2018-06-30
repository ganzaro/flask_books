from . repository import PublisherRepository
from books.app import db

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
        return self.repo.get_one(self.id)


class AddPublisherUseCase():

    def __init__(self, repo=None):
        self.repo = repo or PublisherRepository()

    def set_params(self, publisher):
        self.publisher = publisher


    def execute(self):
        db.session.add(self.publisher)
        db.session.commit()







