import pytest
from app.models import domo_reserva, db
from datetime import date, timedelta
from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy

@pytest.fixture()
def app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = 'Secret'
    #app.config["SQLALCHEMY_DATABASE_URI"]= 'postgresql://postgres:ag@localhost:5432/GPS_TESTING'   #exe
    #app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:peterfields@127.0.0.1:5432/domo-local'     #bdd local nachito
    #app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:admin@127.0.0.1:5432/DOMO-LOCAL'     #bdd local tefy  #bdd servidor ubb
    app.config['SECURITY_PASSWORD_HASH'] = 'scrtcript'
    app.config['SECURITY_PASSWORD_SALT'] = 'fhasdgihwntlgy8f'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    from webpay import bp as webpay_plus_bp
    app.register_blueprint(webpay_plus_bp, url_prefix="/webpay-plus")

    from app import models, views,module

    models.db.init_app(app)

    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

    # clean up / reset resources here

@pytest.fixture()
def client(app):
    return app.test_client()

#### Reservas ####
def test_create_reserva():

    reserva = domo_reserva(rsv_id = 277, rsv_estado = "PRUEBA")
    
    assert reserva.rsv_id == 277
    assert reserva.rsv_estado == "PRUEBA"
    
def test_change_to_fallido():

    reserva = domo_reserva(rsv_id = 277, rsv_estado = "PRUEBA")
    reserva.rsv_estado = "FALLIDO"
    assert reserva.rsv_estado == "FALLIDO"
    
def test_verify_fecha():
    reserva = domo_reserva(rsv_id = 277, rsv_estado = "PRUEBA", rsv_fecha = date.today()+timedelta(days=1), rsv_fechaderegistro = date.today())
    assert reserva.verify_fecha()

def test_verify_fecha_false():
    reserva = domo_reserva(rsv_id = 277, rsv_estado = "PRUEBA", rsv_fecha = date.today(), rsv_fechaderegistro = date.today()+timedelta(days=1))
    assert reserva.verify_fecha() == False

########
