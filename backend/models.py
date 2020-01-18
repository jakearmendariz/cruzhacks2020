from app import mongo

class User(Document):
    username = StringField()
    passwordHash = StringField() # TODO: Samuel Schmidt 1/18/2020 figure out what hashing we want to use
    email = StringField()
    isCharity = BooleanField()
