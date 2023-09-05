from infrastructure.repository.repository_interface import repository_interface
from domain.user import user as users

class user_service:
    def __init__(self,session):
        self.repo = repository_interface(session)
    def register(self,username,password):
        user = users(username=username,password = password)
        return self.repo.register(username,password)
    def login(self,username,password):
        user = users(username=username,password=password)
        return self.repo.login(username,password)
    