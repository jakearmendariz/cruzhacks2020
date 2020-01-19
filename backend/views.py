# views file where we control the views

from app import app
from models import *
from forms import *
from flask import Flask, render_template, request, redirect, url_for

from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField
from wtforms.validators import DataRequired, Length

#@app.route('/result', methods=['POST'])
#def createUser():
#    name = request.form['name']
#    username = request.form['username']
#    password = request.form['password']
#    user = User(name, username, password)
#    user.create()
#    return render_template("result.html")

@app.route('/<string:page_name>/', methods=['POST'])
def renderPosts(page_name):

    if page_name == 'signupSuccess':
        try:
            result = request.form
            User.signup(result)
            return redirect(url_for('index'))
        except:
            return redirect(url_for('signupError'))

    return render_template('%s.html' % page_name)

@app.route('/signupError')
def signupError():
    return render_template('signupError.html')

@app.route('/<string:page_name>/', methods=['GET'])
def renderGets(page_name):
    return render_template('%s.html' % page_name)
 
@app.route('/')
def index():
    return render_template("index.html") 


