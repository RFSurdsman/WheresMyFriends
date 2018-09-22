from flask import render_template, request, url_for, redirect
from flask_login import logout_user, current_user, login_required, login_user
from user import *
from server import app, login, users



def validate_login(username, password):
	for u in users:
		if username == u.username and password == u.password:
		    return u
	return None	

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		print(request.form)
		username = request.form['username']
		password = request.form['password']

		user = validate_login(username, password)

		if user is None:
			print("puck")
		else:
			login_user(user)
			print("wowowowojfijpaojsad!")
			return redirect(url_for('map'))

	return render_template("index.html")

@app.route('/map')
#@login_required
def map():
    return render_template("map.html")

@app.route('/logout')
@login_required
def logout():
	logout_user()
	return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
	global users
	if request.method == 'POST':
		username = request.form['Username']
		password = request.form['Password']

		path = './static/' + current_user.username + '.jpg'
		user = User(username, password, path)
		users.append(user)

		return render_template()
	else:
		return render_template()	

