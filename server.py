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

users = [User("natalie", "k", "nat", (33.919000, 151.221402), "Walkway"), User("rich", "k", "richard", (33.916000, 151.221402), "Parking"), User("kirsten", "k", "kirsten", (33.918000, 151.261402), "Physics Lawn"), User("ryan", "k", "ryan", (33.919000, 151.181402), "Hilmer Building"), User("tone", "k", "tony", (33.918000, 151.221402), "Walkway")]

def get_user(user_id):
	for u in users:
		if u.get_ID == user_id:
			return u
	return None		