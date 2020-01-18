from flask import Flask, render_template
from flask_pymongo import PyMongo
from os import environ

app = Flask(__name__)

app.config.from_envvar('APP_SETTINGS')

mongo = PyMongo(app)

@app.route('/')
def greeter():
    return "Hello World!"