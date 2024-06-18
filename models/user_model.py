from .base_model import BaseModel
from . import db

class User(BaseModel):
    __tablename__ = 'users'

    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)

def get_all_users():
    return User.query.all()

def get_user(user_id):
    return User.query.get(user_id)

def create_user(name, age):
    user = User(name=name, age=age)
    user.save()
    return user

def update_user(user_id, name, age):
    user = User.query.get(user_id)
    if user:
        user.name = name
        user.age = age
        user.save()

def delete_user(user_id):
    user = User.query.get(user_id)
    if user:
        user.delete()