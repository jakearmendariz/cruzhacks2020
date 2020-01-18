from app import mongo
from mongoengine import StringField

class User(dict):
    """
    Basic user object
    """
    id = ""
    name = StringField()
    email = StringField()
    passwordHash = ""

    def create(self):
        pass
    def read(self):
        pass
    def update(self):
        pass
    def delete(self):
        pas