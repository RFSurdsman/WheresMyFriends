from flask import Flask
from routes import app

if __name__ == "__main__":
    app.run(debug = True)

<<<<<<< HEAD
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tasks')
def todos():
    global tasks
    return jsonify(tasks=tasks)

@app.route('/tasks/new', methods=['POST'])
def new_todo():
    id = 0
    print(request.json)
    return jsonify({"title": request.json['title'],
                    "description": request.json['description'],
                    "returnx" : "added from the web server using ajax!!",
                    "id": id})

@app.route('/richard', methods = ['POST', 'GET'])
def richard():
    return render_template('richardmaps.html')


if __name__ == '__main__':
    app.run(debug = "true")

