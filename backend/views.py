# views file where we control the views

from app import app, mongo
from models import *
from forms import *
from flask import Flask, render_template, request, url_for, redirect

from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField
from wtforms.validators import DataRequired, Length

from pymongo import errors

#@app.route('/result', methods=['POST'])
#def createUser():
#    name = request.form['name']
#    username = request.form['username']
#    password = request.form['password']
#    user = User(name, username, password)
#    user.create()
#    return render_template("result.html")


@app.route('/charity/<string:name>')
def displayCharity(name):
    cursor = mongo.db.Charity.find_one_or_404({'name': name})
    
    #nameis = cursor.name
   # email = cursor.email
    #return 'my name is ' + nameis + ", " + email
    return f'''
        <h1>{cursor['name']}</h1>
        <p>{cursor['email']}</p>
        <p>{cursor['website']}</p>
        <p>Who are we?<br>{cursor['Description']}</p>
    '''


@app.route('/<string:page_name>/', methods=['POST'])
def renderPosts(page_name):
    if page_name == 'addSuccess':
        try:
            result = request.form
            charity = Charity(result.get('name'),
                          result.get('email'),
                          result.get('website'),
                          result.get('description'),
                          result.get('pass'))
            charity.dbInsert()
            return redirect(url_for('index'))
        except errors.DuplicateKeyError:
            return render_template('addCharity.html', exception = "Email already in use")

    if page_name == 'signupSuccess':
        try:
            result = request.form
            User.signup(result)
            return redirect(url_for('index'))
        except errors.DuplicateKeyError:
            return render_template('signup.html', exception = "Email already in use")
    if page_name == 'loginSuccess':
        try:
            result = request.form
            User.login(result)
            return redirect(url_for("index"))
        except TypeError as issue:
            return render_template("login.html", exception = "User does not exist")
        except Exception as issue:
            return render_template("login.html", exception = issue)
        except:
            return render_template("loginError".html, exception = "I don't know")
    return render_template('%s.html' % page_name) 

@app.route('/loginError')
def loginError():
    return render_template('loginError.html')

@app.route('/signupError')
def signupError():
    return render_template('signupError.html')

@app.route('/<string:page_name>/', methods=['GET'])
def renderGets(page_name):
    return render_template('%s.html' % page_name)
 
@app.route('/')
def index():
    return render_template("index.html") 
