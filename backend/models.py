from app import mongo
from hashlib import sha224

from util import *

class User(dict):
    """
    Basic user object
    """
    id = ""
    name = ""
    email = ""
    passwordHash = ""

    def __init__(self,
                 name,
                 email,
                 password):

        self.id = sha224(email).hexdigest() 
        self.name = name
        self.email = email
        self.passwordHash = hash_password(password)

    # create a new user from a dictionary
    @staticmethod
    def createFromDict(dict):
        user = User(dict['name'],
                    dict['username'],
                    dict['pass'])
        return user

    # signup a user
    @staticmethod
    def signup(dict):
        user = User.createFromDict(dict)
        user.dbInsert()
    

    # simply return the response of the created login
    def dbInsert(self):
        return mongo.db.User.insert_one({
            "_id": self.id,
            'name': self.name,
            'email': self.email,
            'passwordHash': (self.passwordHash).encode('utf-8')
        })

    # read in the response 
    def dbRead(self):
        pass

    # update the existing user
    def dbUpdate(self):
        pass
    
    # delete a user
    def dbDelete(self):
        pass