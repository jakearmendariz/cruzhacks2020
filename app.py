# main app sequence, how it's going to start

from flask import Flask
from flask_pymongo import PyMongo
from os import environ

app = Flask(__name__)
app.secret_key = "6130559920e1b0777167e23c1420856c914ae5b8"

app.config.from_pyfile('config.py')
mongo = PyMongo(app)

from views import *
from models import *

if __name__ == '__main__':
    app.run()