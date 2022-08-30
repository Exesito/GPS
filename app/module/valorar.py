from app import app, models
from app.forms import RegisterForm, ReservaForm, MesaForm, ClientForm
from app.models import domo_cliente, domo_reserva, domo_restaurante, domo_valoracion
from flask import render_template, request, url_for, redirect, session
from sqlalchemy import func

db = models.db

#### Caso de Uso 2 - Ernesto Opazo ####

@app.route('/valorar/<rsv_id>', methods=['GET','POST'])
def valorar_add(rsv_id):
    
    if request.method == 'POST':
        
        text = request.form["comentario"]
        valor = request.form["valoracion"]    
            
        domo_valoracion.valorar(rsv_id, text, valor)
        
        return redirect(url_for('cli_ver_reservas', cli_id = session['cli_id']))
    
    return render_template("valorar/valorar_add.html", rsv_id = rsv_id)

@app.route('/valoracion/<rsv_id>', methods=['GET','POST'])
def valorar_view(rsv_id):
    
    valoracion = domo_valoracion.query.filter(domo_valoracion.rsv_id == rsv_id).first()
    
    if(valoracion is None):
        return redirect(url_for('valorar_add', rsv_id = rsv_id))
    
    return render_template("valorar/valorar_view.html", rsv_id = rsv_id, valoracion = valoracion)

@app.route('/restaurante/<rtr_id>/valoraciones/', methods=['GET','POST'])
def valorar_list(rtr_id):
    
    valoraciones = domo_restaurante.get_valoraciones(rtr_id)
    
    return render_template("valorar/list_valoraciones.html", valoraciones = valoraciones)

@app.route('/valoracion/delete/<rsv_id>', methods=['GET','POST'])
def valorar_delete(rsv_id):
    
    domo_valoracion.delete(rsv_id)
    
    return redirect(url_for('cli_ver_reservas', cli_id = session['cli_id']))

#### Fin de Caso de uso ###