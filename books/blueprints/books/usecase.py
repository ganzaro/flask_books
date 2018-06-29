from . repository import PublisherRepository

class GetPublishersUseCase():

    def __init__(self, repo=PublisherRepository):
        self.repo = repo()

    def execute(self):
        return self.repo.get_all()

