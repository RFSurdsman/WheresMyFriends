from flask import Flask, render_template, request, jsonify, _app_ctx_stack



app = Flask(__name__)
app.config.from_object(__name__)
tasks = [
        {"title": "Name", "description": "Description"},
        {"title": "Another puck", "description": "asd;kdlkads"},
        {"title": "tony is trash", "description": "lelelelelelle"}
    ] 

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

if __name__ == '__main__':
    app.run()





