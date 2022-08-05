from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SECRET_KEY"] = 'Secret'
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://g25proyecto:g25proyecto1061@146.83.198.35:5432/g25proyecto_bd'


from app import models, views

models.db.init_app(app)