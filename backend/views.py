# views file where we control the views

from app import app

@app.route('/')
def index():
    return '<h1>You are at the index!</h1>'

@app.route('/wrongPlace')
def wrongPlace():
    return 'You aren\'t in the correct place'