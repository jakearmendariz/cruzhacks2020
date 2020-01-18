# views file where we control the views

from app import app
from models import *
from flask import Flask, render_template

# have the mother fucking frontend redirect to this url and the get inserted into the db
@app.route('/<string:page_name>/')
def render_static(page_name):
    return render_template('%s.html' % page_name)
 
 
#@app.route('/')
#def index():
#    return '../templates/index.html'


@app.route('/signup', methods=['POST'])
def createUser():
    name = request.form['name']
    username = request.form['username']
    password = request.form['password']
    user = User(name, username, password)
    user.create()
    print("FUCK SOCIETY AND THEIR GODDAM RULES")
    return name