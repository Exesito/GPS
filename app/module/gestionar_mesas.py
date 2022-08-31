from email import message
from app import app
from app import models as db
from app.models import domo_restaurante

from flask import render_template, request,session, redirect,url_for
from sqlalchemy import func

@app.route('/gestionar_mesas/<rtr_id>')
def gestionar_mesas(rtr_id):
    mesas = db.db.session.query(db.domo_restaurante.rtr_cantidadmesas).filter(db.domo_restaurante.rtr_id==rtr_id).first()
    sillas = db.db.session.query(db.domo_restaurante.rtr_cantidadsillas).filter(db.domo_restaurante.rtr_id==rtr_id).first()
    return render_template("gestionar restaurantes/gestionar_mesas.html", mesas=mesas, sillas=sillas, rtr_id=rtr_id)

@app.route('/gestionar_mesas/editar/<rtr_id>', methods=['POST'])
def editar_mesas(rtr_id):  
    
    if request.method == "POST":
        
        restaurante = domo_restaurante.query.filter(db.domo_restaurante.rtr_id==rtr_id).first()
        restaurante.rtr_cantidadmesas = request.form["mesas"]
        restaurante.rtr_cantidadsillas = request.form["sillas"]
        db.db.session.commit()
        
    return redirect(url_for('gestionar_mesas', rtr_id = rtr_id))