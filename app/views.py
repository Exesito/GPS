from app import app, models
from flask import render_template

db = models.db

@app.route('/')
def index():
    
    new_user = models.User(id = 1, email = 'aaaa@gmail.com', password = b'ewe')
    print(new_user.verify_password(b'ewe'))
    print(new_user.password)
    
    return render_template("home.html")