from app import app
from flask import render_template, request

@app.route('/')
def index():
    return render_template("home.html")

@app.errorhandler(404)
def not_found(e):
    
    return render_template("errors/404.html")

@app.errorhandler(500)
def server_error(e):
    
    return render_template("errors/500.html")