from domain.models.usermodel import usermodel,db
from domain.user import user as users

class repository_interface:
    def __init__(self,session):
        self.session= session
    def register(self,username,password):
        user = usermodel(username=username,password=password)
        self.session.add(user)
        self.session.commit()
        return user
    