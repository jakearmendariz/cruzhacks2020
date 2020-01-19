from app import mongo
from hashlib import sha224

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
                 passwordHash):

        self.id = sha224(email).hexdigest() 
        self.name = name
        self.email = email
        self.passwordHash = passwordHash

    # create a new user from a dictionary
    @staticmethod
    def createFromDict(dict):
        user = User(dict['name'],
                    dict['username'],
                    dict['pass'])
        return user

    # simply return the response of the created login
    def dbInsert(self):
        return mongo.db.User.insert_one({
            'name': self.name,
            'email': self.email,
            'passwordHash': self.passwordHash
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