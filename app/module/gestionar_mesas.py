from app import app
from app import models as db

from flask import render_template, request,session, redirect,url_for
from sqlalchemy import func

@app.route('/gestionar_mesas/<rtr_id>')
def gestionar_mesas(rtr_id):
    mesas = db.db.session.query(db.domo_restaurante.rtr_cantidadmesas).filter(db.domo_restaurante.rtr_id==rtr_id).first()
    sillas = db.db.session.query(db.domo_restaurante.rtr_cantidadsillas).filter(db.domo_restaurante.rtr_id==rtr_id).first()
    return render_template("gestionar restaurantes/gestionar_mesas.html", mesas=mesas, sillas=sillas)