from . repository import PublisherRepository

class GetPublishersUseCase():

    def __init__(self, repo=None):
        # if repo is None:
        #     repo = PublisherRepository()
        self.repo = repo or PublisherRepository()

    def execute(self):
        return self.repo.get_all()


class GetPublisherUseCase():

    def __init__(self, repo=None):
        if repo is None:
            repo = PublisherRepository()
        self.repo = repo

    def set_params(self, id):
        self.id = id

    def execute(self):
        return self.repo.get_one(self.id)

