# views file where we control the views

from app import app
from models import *

# have the mother fucking frontend redirect to this url and the get inserted into the db
@app.route('/')
def index():
    user = User("Samuel Schmidt",
                 "sam@somewhere.com",
                 "asdf")
    
    return 'Created user with id of {0}'.format(user.create())

@app.route('/wrongPlace')
def wrongPlace():
    return 'You aren\'t in the correct place'