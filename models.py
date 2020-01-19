from app import mongo
from hashlib import sha224

from util import *

import json

class Charity(object):
    id = ""
    name = ""
    email = ""
    password = ""
    description = ""
    img = ""
    charType = ""
    website = ""
    
    def __init__(self,
                 name,
                 email,
                 website,
                 description,
                 img,
                 charType,
                 passwordHash):#Add in image later

        self.id = sha224(email.encode('utf-8')).hexdigest() 
        self.name = name
        self.email = email
        self.website = website
        self.description = description
        self.img = img
        self.type = charType
        self.password = hash_password(passwordHash)
    
      # create a new user from a dictionary
    @staticmethod
    def createFromDict(dict):
        charity = Charity(
                    dict['name'],
                    dict['username'],
                    dict['website'],
                    dict['description'],
                    dict['img'],
                    dict['pass'])
                    #dict['img'])
        return charity

    # simply return the response of the created login
    def dbInsert(self):
        return mongo.db.Charity.insert_one({
            '_id': self.id,
            'name': self.name,
            'email': self.email,
            'website':self.website,
            'description':self.description,
            'img': self.img,
            'type': self.type,
            'passwordHash': self.password
            #'img':self.img
        })
    
     # read in the response
    def dbRead(self):
        # TODO: Samuel Schmidt implement this for logging in        
        pass

    # update the existing user
    def dbUpdate(self):
        pass
    
    # delete a user
    def dbDelete(self):
        pass
 


class User(object):
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

        self.id = sha224(email.encode('utf-8')).hexdigest() 
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
        return user.dbInsert()

    @staticmethod
    def login(dict):
        user = User("",
                    dict.get('username'),
                    dict.get('pass'))
        userDict = user.dbRead()
        if not verify_password(userDict['passwordHash'], dict.get('pass')):
            raise Exception("Invalid password")
        return userDict
    

    # simply return the response of the created login
    def dbInsert(self):
        return mongo.db.User.insert_one({
            "_id": self.id,
            'name': self.name,
            'email': self.email,
            'passwordHash': (self.passwordHash)
        })

    # read in the response 
    def dbRead(self):
        document = mongo.db.User.find_one({"_id": self.id})
        return document

    # update the existing user
    def dbUpdate(self):
        pass
    
    # delete a user
    def dbDelete(self):
        pass