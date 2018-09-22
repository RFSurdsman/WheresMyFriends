from flask import Flask
from flask_login import LoginManager
from user import *

app = Flask(__name__)
login = LoginManager(app)

login.init_app(app)
login.login_view = 'login'

@login.user_loader
def load_user(user_id):
	return get_user(user_id)

users = [User("kirsten", "k", "kirsten")]

def get_user(user_id):
	for u in users:
		if u.get_ID == user_id:
			return u
	return None		