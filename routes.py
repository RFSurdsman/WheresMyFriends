from flask import Flask, render_template, request, jsonify, _app_ctx_stack

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def login():
    return render_template("index.html")