from faulthandler import disable
from app import app, models, functions
from app.forms import RegisterForm, ReservaForm, MesaForm, ClientForm
from app.models import domo_cliente, domo_reserva, domo_restaurante, domo_valoracion, domo_horario
from flask import render_template, request, url_for, redirect, session
from sqlalchemy import func
from datetime import timedelta, date, datetime

db = models.db

####-- Caso de uso realizar reserva - Ernesto Opazo --####

@app.route('/reservar/<id>', methods=['GET','POST'])
def reservar(id):
    
    day_choice = [1,2,3]
    
    horario = domo_horario.query.filter(domo_horario.rtr_id == id).first()
    
    hour_choice = []
    disable_hour = False
    
    if horario != None:
        i = horario.hor_horainicio.hour
        print(i)
        while i < horario.hor_horatermino.hour:
            
            hour_choice.append(i)
            i = i + 1
    else:
        disable_hour = True
    
    form = ReservaForm()
    mesa_form = MesaForm()
    client_form = ClientForm()
    
    form.dia.choices = day_choice
    form.hora.choices = hour_choice
    
    restaurante = models.domo_restaurante.get_by_id(id)
    mesas = restaurante.get_mesas()

    disable_form = False
    
    if len(mesas) < 1:
        disable_form = True
    
    for item in mesas:
        mesa_form.mesa.choices.append((item.msa_id, item.msa_numero))
    
    data = {
        "RESTAURANTE_ID": restaurante.rtr_id,
        "nombre": restaurante.rtr_nombre,
        "descripcion": restaurante.rtr_descripcion
    }
    
    valoraciones = domo_restaurante.get_valoraciones_max(id, 3)
    
    return render_template("reserva/cli_reservar.html", data = data, form = form, mesa_form = mesa_form, client_form = client_form, valoraciones=valoraciones, disable_form = disable_form, disable_hour = disable_hour)

@app.route('/reservar/<id_restaurante>/<id_reserva>/datos_cliente', methods=['GET','POST'])
def reserva_not_registered(id_restaurante, id_reserva):
    
    client_form = ClientForm()  
    restaurante = models.domo_restaurante.get_by_id(id_restaurante)
    
    data = {
        "RESTAURANTE_ID": restaurante.rtr_id,
        "nombre": restaurante.rtr_nombre,
        "descripcion": restaurante.rtr_descripcion,
        "id_reserva": id_reserva
    }
    
    return render_template("reserva/cli_reservar_not_registered.html", data = data, client_form = client_form)

@app.route('/reservar/<id_restaurante>/<id_reserva>/create_new_client/', methods=['GET','POST'])
def reserva_new_client(id_restaurante, id_reserva):
    
    if request.method == 'POST':
    
        nombre = request.form["nombre"]
        apellido = request.form["apellido"]
        telefono = request.form["telefono"]
        rut = request.form["rut"]
        medio_de_pago = request.form["medio_de_pago"]
        email = request.form["email"]
        
        reserva = domo_reserva.get_by_id(id_reserva)
        
        cliente = domo_cliente.get_by_rut(rut)
        
        if cliente is not None:
            cliente.cli_telefono = telefono
        else:
            max_id_cli = models.db.session.query(func.max(models.domo_cliente.cli_id)).scalar() + 1
            cliente = domo_cliente(cli_id = max_id_cli, cli_nombre=nombre, cli_apellido=apellido, cli_telefono=telefono, cli_rut = rut, cli_correo = email)
            db.session.add(cliente)
        
        dict_mdp = {
            "DEBITO": 1,
            "EFECTIVO": 2,
            "WEBPAY": 3
        }        
      
        reserva.cli_id = cliente.cli_id
        reserva.tpr_id = dict_mdp[medio_de_pago]
        reserva.estado = "PROCESANDO"
        
        db.session.commit()
        
        if medio_de_pago == "WEBPAY":
            return redirect(url_for('webpay_plus.create', rsv_id = id_reserva, cli_id = cliente.cli_id))
        
        return redirect(url_for('reserva_exitosa', id_restaurante = id_restaurante, id_reserva = id_reserva))#retorna reserva exitosa

@app.route('/reservar/<id_restaurante>/generar_reserva', methods=['GET','POST'])
def reserva_create(id_restaurante):
    
    if request.method == 'POST':
        
        hora = request.form['hora']
        fecha = request.form["dia"]
        mesa_id = request.form['mesa']
        estado = "PROCESANDO"
        
        restaurante = domo_restaurante.get_by_id(id_restaurante)
        id_reserva = restaurante.generate_reserva(hora, fecha, mesa_id, estado)
        
        reserva = domo_reserva.get_by_id(id_reserva)
        
        if session.get('cli_id') is None:
            return redirect(url_for('reserva_not_registered', id_restaurante = id_restaurante, id_reserva = id_reserva))
        
        medio_de_pago = request.form["medio_de_pago"]
        
        dict_mdp = {
            "DEBITO": 1,
            "EFECTIVO": 2,
            "WEBPAY": 3
        }
        
        reserva.cli_id = session["cli_id"]
        reserva.tpg_id = dict_mdp[medio_de_pago] 
        db.session.commit()
        
        if medio_de_pago == "WEBPAY":
            return redirect(url_for('webpay_plus.webpay_plus_create', rsv_id = id_reserva, cli_id = session["cli_id"]))
        
        
        return redirect(url_for('reserva_exitosa', id_restaurante = id_restaurante, id_reserva = id_reserva))

@app.route('/reservar/<id_restaurante>/<id_reserva>/reserva_exitosa', methods=['GET','POST'])
def reserva_exitosa(id_restaurante, id_reserva):
    
    restaurante = models.domo_restaurante.get_by_id(id_restaurante)
    reserva = models.domo_reserva.get_by_id(id_reserva)
    cliente = models.domo_cliente.get_by_id(reserva.cli_id)
    mesa = models.domo_mesa.get_by_id(reserva.msa_id)
    
    if reserva.rsv_estado != "PROCESANDO" :
        return redirect(url_for('index'))
    
    reserva.rsv_estado = "CREADA"
    db.session.commit()
    
    mensaje =  "Su reserva a sido aprobada para el dia " + str(reserva.rsv_fecha) + " a las " + str(reserva.rsv_hora)
    mensaje =  mensaje + ", con codigo " + str(reserva.rsv_id)
    functions.enviar_email_cliente(reserva.get_cliente(), mensaje, "Reserva realizada con exito")
    
    return render_template("reserva/cli_reserva_exitosa.html", restaurante=restaurante, reserva=reserva, cliente=cliente, mesa = mesa)

@app.route('/reservar/error', methods=['GET','POST'])
def reserva_error():
    
    return render_template("reserva/cli_reserva_fallida.html")

@app.route('/cliente/<cli_id>/ver_reservas', methods=['GET','POST'])
def cli_ver_reservas(cli_id):
    
    if int(session["cli_id"]) != int(cli_id):
        return redirect(url_for('cli_ver_reservas', cli_id= cli_id))
    
    reservas = domo_cliente.get_reservas(cli_id)
    
    return render_template("reserva/cli_ver_reservas.html", reservas=reservas, cli_id = cli_id)

@app.route('/restaurante/<rtr_id>/ver_reservas', methods=['GET','POST'])
def res_ver_reservas(rtr_id):
    
    if int(session["rtr_id"]) != int(rtr_id):
        return redirect(url_for('res_ver_reservas', rtr_id = rtr_id))
    
    reservas = domo_restaurante.get_reservas(rtr_id)
    
    return render_template("reserva/res_ver_reservas.html", reservas = reservas, rtr_id=rtr_id)

@app.route('/restaurante/<rtr_id>/ver_reservas/aprobar/<rsv_id>')
def aprobar_reserva(rtr_id, rsv_id):
    
    if int(session["rtr_id"]) != int(rtr_id):
        return redirect(url_for('res_ver_reservas', rtr_id = rtr_id))
    
    domo_reserva.get_by_id(rsv_id).rsv_estado = "REALIZADA"
    db.session.commit()
    
    return redirect(url_for('res_ver_reservas', rtr_id = rtr_id))

@app.route('/restaurante/<rtr_id>/ver_reservas/cancelar/<rsv_id>')
def cancelar_reserva(rtr_id, rsv_id):
    
    if int(session["rtr_id"]) != int(rtr_id):
        return redirect(url_for('res_ver_reservas', rtr_id = rtr_id))
    
    domo_reserva.get_by_id(rsv_id).rsv_estado = "CANCELADA"
    db.session.commit()
    
    return redirect(url_for('res_ver_reservas', rtr_id = rtr_id))

@app.route('/cliente/<cli_id>/ver_reservas/cancelar/<rsv_id>')
def cli_cancelar_reserva(cli_id, rsv_id):
    
    if int(session["cli_id"]) != int(cli_id):
        return redirect(url_for('cli_ver_reservas', cli_id = cli_id))
    
    domo_reserva.get_by_id(rsv_id).rsv_estado = "CANCELADA"
    db.session.commit()
    
    return redirect(url_for('cli_ver_reservas', cli_id = cli_id))

####-- FIN DE CASO DE USO --####