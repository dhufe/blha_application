
from flask import Flask
from flask import g
from flask import redirect
from flask import request
from flask import session
from flask import url_for, abort, render_template, flash
from functools import wraps
from haslib import md5
from peewee import *

### config part 
DATABASE = 'user_database.db'
DEBUG = True
### config done


appfe = Flask(__name__)
appfe.config.from_object(__name__)

database = SqliteDatabase(DATABASE)

# virutal class model, as simple interface if in future multiple tables needed
class BaseModel(Model):
    class Meta:
        database = database

# implement a basic user
class User(BaseModel):
    username = CharField(unique = True)
    password = CharField()

def create_tables():
    with database:
        database.create_tables([User])

def auth_user(user):
    session['logged_in'] = True
    session['user_id'] = user.id
    session['username'] = user.username

    flash('You are logged in as %s.' % (user.username) )

def get_current_user():
    if session.get('logged_in'):
        return User.get( User.id == session['user_id'])

def login_required(f):
    @wraps(f)
    def inner(*args, **kwargs):
        if not session.get('logged_in'):
            return redirect( url_for('login') )
        return f(*args, **kwargs)
    return inner

### appfe code

@appfe.before_request
def before_request():
    g.db = database
    g.db.connect()

@appfe.after_request
def after_request(response):
    g.db.close()
    return response

# views

@appfe.route('/')
def homepage():
    #if session.get('logged_in'):
    
    
@appfe.route('/login/', method=['GET', 'POST'])
def login():


@appfe.route('/logout/')
def logout():
    session.pop('logged_in', None )
    flash('You were logged out.')
    return redirect(url_for('homepage'))


