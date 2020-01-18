# views file where we control the views

from app import app

@app.route('/')
def index():
    return '../templates/index.html'

@app.route('/wrongPlace')
def wrongPlace():
    return 'You aren\'t in the correct place'