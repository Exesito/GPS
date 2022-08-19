from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from notifypy import Notify

app = Flask(__name__)
app.config["SECRET_KEY"] = 'Secret'
#app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:peterfields@127.0.0.1:5432/domo-local'     #bdd local nachito
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://g25proyecto:g25proyecto1061@146.83.194.142:5432/g25proyecto_bd'   #bdd servidor ubb
app.config['SECURITY_PASSWORD_HASH'] = 'scrtcript'
app.config['SECURITY_PASSWORD_SALT'] = 'fhasdgihwntlgy8f'

from app import models, views

models.db.init_app(app)