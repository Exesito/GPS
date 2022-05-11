from app import app, models
from flask import render_template

db = models.db

@app.route('/')
def index():

    return render_template("home.html")