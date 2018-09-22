from flask import render_template, request, url_for
from flask_login import logout_user, current_user
from user import *

users = []

def validate_login(username, password):
	for u in users:
		if username == u.username and password == p.password
		return user
	return None	

@app.route('/')
def index():
	return render_template()


@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		username = request.form['Username']
		password = request.form['Password']


		user = validate_login(username, password)

		if user is None:
			return
		else:
			login_user
			redirect(url_for('map'))

@app.route('/map')
@login_required
def map():




@app.route('/logout')
@login_required
def logout():
	logout_user()
	return redirect(url_for('index'))

@app.route('/register', methods=['GET'. 'POST'])
	if request.method == 'POST':
		username = request.form['Username']
		password = request.form['Password']

		user = User(username, password)
		users.add(user)

		return render_template()
	else:
		return render_template()	

