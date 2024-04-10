from flask import Flask
from flask import redirect
from flask import request
from flask import session
from flask import url_for, render_template, flash

from functools import wraps
import requests


# config part
PORT = 8080
DEBUG = True
SECRET_KEY = 'hin6bab8ge25*r=x&amp;+5$0kn=-#log$pt^#@vrqjld!^2ci@g*b'
BACKEND_URL = 'http://127.0.0.1:8001/users/'
# config done
appfe = Flask(__name__)
appfe.config.from_object(__name__)


def auth_user(username, uid):
    session['logged_in'] = True
    session['user_id'] = uid
    session['username'] = username

    flash('You are logged in as %s.' % username)


# def get_current_user():
#     if session.get('logged_in'):
#         return User.get(User.id == session['user_id'])


def login_required(f):
    @wraps(f)
    def inner(*args, **kwargs):
        if not session.get('logged_in'):
            return redirect(url_for('login'))
        return f(*args, **kwargs)

    return inner


# appfe code
@appfe.route('/')
def homepage():
    if session.get('logged_in'):
        return user_list()

    return render_template('homepage.html')


@appfe.route('/users/')
def user_list():
    users = requests.get(BACKEND_URL)
    return render_template('user_list.html', jsnObj=users.json())


@appfe.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST' and request.form['username']:
        response = requests.get(BACKEND_URL)
        response.raise_for_status()

        users = response.json()

        for j in users:
            if j['username'] == request.form['username'] and j['password'] == request.form['password']:
                auth_user(j['username'], j['id'])
                return redirect(url_for('homepage'))

    return render_template('login.html')


@appfe.route('/logout/')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out.')
    return redirect(url_for('homepage'))


@appfe.route('/create/', methods=['GET', 'POST'])
def create():
    if request.method == 'POST' and request.form['username']:
        payload = {'username': request.form['username'], 'password': request.form['password']}
        header = {'Content-type': 'application/json', 'Accept': 'text/plain'}

        requests.post('http://backend:8001/create/', json=payload, headers=header)
        return redirect(url_for('homepage'))

    return render_template('create.html')


if __name__ == '__main__':
    appfe.run(host="0.0.0.0", port=PORT)
