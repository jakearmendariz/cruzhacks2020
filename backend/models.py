from app import mongo

class User(dict):
    """
    Basic user object
    """
    name = ""
    email = ""
    passwordHash = ""

    def __init__(self,
                 name,
                 email,
                 passwordHash):

        self.name = name
        self.email = email
        self.passwordHash = passwordHash

    # simply return the response of the created login
    def create(self):
        return mongo.db.User.insert_one({
            'firstName': self.firstName,
            'middleName': self.middleName,
            'lastName': self.lastName,
            'email': self.email,
            'passwordHash': self.passwordHash
        })

    # read in the response 
    def read(self):
        pass

    # update the existing user
    def update(self):
        pass
    
    # delete a user
    def delete(self):
        pass