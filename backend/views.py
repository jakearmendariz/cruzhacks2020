# views file where we control the views

from app import app, mongo
from models import *
from forms import *
from flask import Flask, render_template, request, url_for, redirect, session

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
    name = name.replace("+", " ")
    cursor = mongo.db.Charity.find_one_or_404({'name': name})
    name = name.title()
    return render_template("charitybase.html", _name = name, _website = cursor['website'], _email = cursor['email'], _description = cursor['description'], _img = cursor['img'])
#    return f'''<img src = "{cursor['img']}">
#                <h1>{name}</h1>
#                <h3>Find us at:{cursor['website']}</h3>
 #               <p>{cursor['description']}</p>
#                <p>If you want to get involved. Email us at {cursor['email']}</p>
#                '''


@app.route('/<string:page_name>/', methods=['POST'])
def renderPosts(page_name):
    if page_name == 'addSuccess':
        try:
            result = request.form
            charity = Charity(result.get('name').lower(),
                          result.get('email'),
                          result.get('website'),
                          result.get('description'),
                          result.get('img'),
                          result.get('type'),
                          result.get('pass'))
                          
            charity.dbInsert()
            return redirect(url_for('index'))
        except errors.DuplicateKeyError:
            return render_template('addCharity.html', exception = "Email already in use")

    if page_name == 'signupSuccess':
        try:
            result = request.form
            User.signup(result)
            session['name'] = result.get('name')
            return redirect(url_for('index'))
        except errors.DuplicateKeyError:
            return render_template('signup.html', exception = "Email already in use")
    if page_name == 'loginSuccess':
        try:
            result = request.form
            User.login(result)
            session['name'] = result.get('name')
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
def render_static(page_name):
    return render_template('%s.html' % page_name)
 
@app.route('/box')
def box_index():
    _items = mongo.db.Charity.find() #This is an array, we have to pass this to the function
    return render_template('box.html', items = _items)
#    return 'Hello world'
#    return render_template('box.html', items = _items)
 
@app.route('/')
def index():
    _items = mongo.db.Charity.find() #This is an array, we have to pass this to the function
    if session.get('name') != None:
        return render_template('index.html', items = _items, value = session.get('name'))
    return render_template('index.html', items = _items, value = "Login")
  