
from flask import Flask
from flask import g
from flask import redirect
from flask import request
from flask import session
from flask import url_for, abort, render_template, flash
from functools import wraps
from hashlib import md5
from peewee import *
import requests

### config part 
PORT     = 8002
DEBUG    = True
ADPW     = 'TestLauf'
### config done


appfe = Flask(__name__)
appfe.config.from_object(__name__)


def auth_user(user):
    session['logged_in'] = True
    session['user_id']   = user.id
    session['username']  = user.username

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

@appfe.route('/')
def homepage():
    if session.get('logged_in'):
        return user_list()
    else:
        return user_list()

@appfe.route('/users/')
def user_list():
    
    users = requests.get('http://127.0.0.1:8001/users/')
    return render_template('user_list.html', jsnObj=users.json() )

    
@appfe.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST' and request.form['username']:
        try:
            print ( 'Login process....')
        except User.DoesNotExist:
            flash('The password entered is incorrect')
        else:
            auth_user(user)
            return redirect(url_for('homepage'))

    return render_template('login.html')


@appfe.route('/logout/')
def logout():
    session.pop('logged_in', None )
    flash('You were logged out.')
    return redirect(url_for('homepage'))


if __name__ == '__main__':
    appfe.run( debug = DEBUG, port = PORT )