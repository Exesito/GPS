from app import app
from app import models as db
from sqlalchemy import true

from flask import render_template, request,session, redirect,url_for
from sqlalchemy import func

@app.route('/buscar_restaurantes')
def buscar_restaurante():
    restaurantes=db.db.session.query(db.domo_restaurante, db.domo_tiporestaurante).filter(
        db.domo_restaurante.tpr_id==db.domo_tiporestaurante.tpr_id,
        db.domo_restaurante.rtr_visible == true()).all()
    tipo=db.db.session.query(db.domo_tiporestaurante).all()
    return render_template("buscar_restaurante/buscar_restaurante.html",restaurantes=restaurantes, tipo=tipo)   