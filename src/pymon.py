import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://readAndWrite:uJkfM1V7bi3xT13k@cluster0-ksxj2.gcp.mongodb.net/User?retryWrites=true&w=majority")
db = cluster["CharityDB"]
collection = db["User"]

post = {"_id":0, "name": "Jake", "happiness_level":0}

collection.insert_one(post)

