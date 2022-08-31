from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from notifypy import Notify
import os



app = Flask(__name__)
app.config["SECRET_KEY"] = 'Secret'
#app.config["SQLALCHEMY_DATABASE_URI"]= 'postgresql://postgres:aaaaa@localhost:5432/postgres'   #exe
#app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:sql@127.0.0.1:5432/DOMO-LOCAL'     #bdd local nachito
#app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://g25proyecto:g25proyecto1061@146.83.194.142:5432/g25proyecto_bd'   #bdd servidor ubb
#app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:peterfields@127.0.0.1:5432/domo-local'     #bdd local nachito
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:sql@127.0.0.1:5432/DOMO-LOCAL'     #bdd local tefy
#app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://g25proyecto:g25proyecto1061@146.83.194.142:5432/g25proyecto_bd'   #bdd servidor ubb
app.config['SECURITY_PASSWORD_HASH'] = 'scrtcript'
app.config['SECURITY_PASSWORD_SALT'] = 'fhasdgihwntlgy8f'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['UPLOAD_FOLDER'] = os.path.join(os.path.expanduser('~'), '/cartas')


from webpay import bp as webpay_plus_bp
app.register_blueprint(webpay_plus_bp, url_prefix="/webpay-plus")

from app import models, views,module

models.db.init_app(app)