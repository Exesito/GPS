from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from notifypy import Notify

app = Flask(__name__)
app.config["SECRET_KEY"] = 'Secret'
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:sql@localhost:5432/DOMO-LOCAL'
app.config['SECURITY_PASSWORD_HASH'] = 'scrtcript'
app.config['SECURITY_PASSWORD_SALT'] = 'fhasdgihwntlgy8f'

from app import models, views, module

models.db.init_app(app)