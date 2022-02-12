import os

from flask import Flask, render_template, request, redirect, session, g
import requests
from sqlalchemy.exc import IntegrityError
from forms import ______
from models import db, connect_db, User, Drink_name

CURR_USER_KEY = "curr_user"

API_BASE_URL = "www.thecocktaildb.com/api/json/v1/1"

# You should keep your API key a secret (I'm keeping it here so you can run this app)
key = '1'

app = Flask(__name__)

connect_db(app)


""""""""""""""""""""""""""""""""""""
"""User Signup/login/logout"""

@app.before_request
def add_user_to_g():
    """If logged in, add current user to Flask global"""

    if CURR_USER_KEY in session:
        g.user = User.query.get(session[CURR_USER_KEY])
    else: g.user = None

def login(user):
    session[CURR_USER_KEY] = user.id

def logout():
    if CURR_USER_KEY in session:
        del session[CURR_USER_KEY]


@app.route('/signup', methods=["GET", "POST"])
def signup():






def get_random_drink(random):
    res = requests.get(f"{API_BASE_URL}/random.php")
    data = res.json()
    return data

