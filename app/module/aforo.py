from app import app, models
from app.forms import RegisterForm, ReservaForm, MesaForm, ClientForm
from app.models import domo_aforo, domo_cliente, domo_reserva, domo_restaurante
from flask import render_template, request, url_for, redirect, session
from sqlalchemy import func

db = models.db

@app.route('/ver_aforo')
def ver_aforo():
    id = session["rtr_id"]
    afo = domo_aforo.query.filter(domo_aforo.rtr_id == id).first()
    if afo == None:
        afo = domo_restaurante.get_by_id(id).get_aforo()
    aforoMax = afo.afo_capacidadmax
    aforo = afo.afo_capacidadactual
    return render_template("aforo/ver_aforo.html", afoM = aforoMax, afo = aforo, rtr_id = id)

@app.route('/ver_aforo/actualizar', methods = ['POST'])
def actualizar_aforo():
    print("Se intenta actualizar el restaurante ")
    if request.method == 'POST':
        print("llega al request method")
        id_restaurante = request.json["id"]
        aforo_nuevo = request.json["aforo"]
        afororest = db.session.query(domo_aforo).filter(domo_aforo.rtr_id == id_restaurante).first()

        if(aforo_nuevo != afororest.afo_capacidadactual):    
            if(aforo_nuevo>0):
                afororest.afo_capacidadactual = min(afororest.afo_capacidadmax, aforo_nuevo)
            else:
                afororest.afo_capacidadactual = 0
            db.session.commit()
    return redirect(url_for("ver_aforo"))


