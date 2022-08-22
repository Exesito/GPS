from app import app, models as db
from flask import render_template



@app.route('/')
def index():
    return render_template("home.html")

