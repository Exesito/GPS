from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SECRET_KEY"] = 'Secret'
#app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://g25proyecto:g25proyecto1061@146.83.198.35:5432/g25proyecto_bd'
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:peterfields@190.47.90.186:5432/domo_testing'


from app import models, views

models.db.init_app(app)