# views file where we control the views

from app import app
from models import *
from flask import Flask, render_template

    
# have the mother fucking frontend redirect to this url and the get inserted into the db
@app.route('/<string:page_name>/', methods=['GET'])
def render_static(page_name):
    return render_template('%s.html' % page_name)
 
@app.route('/')
def index():
    return render_template('index.html')


 
#@app.route('/')
#def index():
#    return '../templates/index.html'


