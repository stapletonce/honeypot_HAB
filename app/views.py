# views.py

from flask import render_template

from app import app

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/<path:path>')
def send(path):
  return app.send_static_file(path)   


@app.route('/system')
def system():
    return render_template("system.html")

@app.route('/logs')
def logs():
    return render_template("logs.html")

@app.route('/editdevice')
def editdevice():
    return render_template("editdevice.html")

@app.route('/login')
def login():
    return render_template("login.html")