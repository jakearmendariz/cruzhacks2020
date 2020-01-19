# views file where we control the views

from app import app, mongo
from models import *
from forms import *
from flask import Flask, render_template, request, url_for, redirect

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


@app.route('/charity/<string:name>')
def displayCharity(name):
    name = name.replace("+", " ")
    cursor = mongo.db.Charity.find_one_or_404({'name': name})
    name = name.title()
    return f'''<h1>{name}</h1>
                <h3>Find us at:{cursor['website']}</h3>
                <p>{cursor['description']}</p>
                <p>If you want to get involved. Email us at {cursor['email']}</p>
                '''
#    return f'''
#        <h1>{cursor['name']}</h1>
#        <p>{cursor['email']}</p>
#        <p>{cursor['website']}</p>
#        <p>Who are we?<br>{cursor['Description']}</p>
#    '''


@app.route('/<string:page_name>/', methods=['POST'])
def renderPosts(page_name):
    if page_name == 'addSuccess':
        result = request.form
        charity = Charity(result.get('name').lower(),
                          result.get('email'),
                          result.get('website'),
                          result.get('description'),
                          result.get('pass'))
        charity.dbInsert()
        return redirect(url_for('index'))
    if page_name == 'signupSuccess':#usersignup
        try:
            result = request.form
            User.signup(result)
            return redirect(url_for('index'))
        except:
            return redirect(url_for('signupError'))
   # el

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
