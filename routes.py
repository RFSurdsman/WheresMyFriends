from flask import render_template, request, url_for, redirect, jsonify
from flask_login import logout_user, current_user, login_required, login_user
from user import *
from server import app, login, users
import geocoder

user = None

def validate_login(username, password):
	for u in users:
		if username == u.username and password == u.password:
		    return u
	return None	

@app.route('/', methods=['GET', 'POST'])
def index():
	global user
	if request.method == 'POST':
		print(request.form)
		username = request.form['username']
		password = request.form['password']

		user = validate_login(username, password)

		if user is None:
			print('puck')
		else:
			login_user(user)
			return redirect(url_for('map'))

	return render_template("index.html")

@login_required
@app.route('/map')
def map():
	global user
	global users
	return render_template("map.html", user = user, users = users)

@login_required
@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
	global users
	if request.method == 'POST':
		username = request.form['Username']
		password = request.form['Password']

		path = current_user.username + '.jpg'
		user = User(username, password, path)
		users.append(user)

		return render_template()
	else:
		return render_template()	

@app.route('/geolocator', methods = ['POST', 'GET'])
def geolocator():
	return render_template('geolocator.html')


@app.route('/poslistener', methods = ['POST', 'GET'])
def poslistener():
	longitude = request.json['longitude']
	latitude = request.json['latitude']
	print(str(user.position))
	user.position = (abs(latitude), longitude)
	print(str(user.position))
	return jsonify({"longitude": request.json['longitude'], 
		"latitude": request.json['latitude']})