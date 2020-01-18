# main app sequence, how it's going to start

from flask import Flask, render_template
from flask_pymongo import PyMongo
from os import environ

app = Flask(__name__)

app.config.from_pyfile('config.py')
mongo = PyMongo(app)

from views import *
from models import *

if __name__ == '__main__':
    app.run()