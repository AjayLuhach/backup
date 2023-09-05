from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
db = SQLAlchemy()

class usermodel(UserMixin,db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer(),nullable = False,primary_key=True)
    username = db.Column(db.String(255),nullable=False)
    password = db.Column(db.String(8),nullable=False)
    __tableargs__ = {'extend_existing':True}