from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config["SECRET_KEY"] = 'Secret'
app.config["SQLALCHEMY_DATABASE_URI"]= 'postgresql://postgres:sheik1245@localhost:5432/GPS'
#app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://g25proyecto:g25proyecto1061@146.83.198.35:5432/g25proyecto_bd'
app.config['SECURITY_PASSWORD_HASH'] = 'scrtcript'
app.config['SECURITY_PASSWORD_SALT'] = 'fhasdgihwntlgy8f'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

from webpay import bp as webpay_plus_bp
app.register_blueprint(webpay_plus_bp, url_prefix="/webpay-plus")

from app import models, views, module

models.db.init_app(app)