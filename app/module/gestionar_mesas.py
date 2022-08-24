from app import app
from app import models as db

from flask import render_template, request,session, redirect,url_for
from sqlalchemy import func

@app.route('/gestionar_mesas')
def gestionar_mesas():
    mesas = db.db.session.query(db.domo_restaurante.rtr_cantidadmesas).filter(db.domo_restaurante.rtr_id==10).first()
    sillas = db.db.session.query(db.domo_restaurante.rtr_cantidadsillas).filter(db.domo_restaurante.rtr_id==10).first()
    return render_template("assets/gestionar_mesas.html", mesas=mesas, sillas=sillas)