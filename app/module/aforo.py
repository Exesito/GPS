from app import app, models
from app.forms import RegisterForm, ReservaForm, MesaForm, ClientForm
from app.models import domo_aforo, domo_cliente, domo_reserva, domo_restaurante
from flask import render_template, request, url_for, redirect, session
from sqlalchemy import func

db = models.db

@app.route('/ver_aforo/<id>')
def ver_aforo(id):
    afo = domo_aforo.get_by_restaurante(id)
    aforoMax = afo.afo_capacidadmaxima
    aforo = afo.afo_capacidadactual
    return render_template('ver_aforo.html', afoM = aforoMax, afo = aforo)

def actualizar_aforo(id, aforo_nuevo):
    afororest = db.session.query(domo_aforo).filter(domo_aforo.rtr_id == id).first()
    
    if(aforo_nuevo != afororest.afo_capacidadactual):    
        if(aforo_nuevo>0):
            afororest.afo_capacidadactual = min(afororest.afo_capacidadmax, aforo_nuevo)
        else:
            afororest.afo_capacidadactual = 0

        db.session.commit()


