
from multiprocessing.connection import Client
from app import app, models
from app.forms import RegisterForm, ReservaForm, MesaForm, ClientForm
from app.models import User, domo_cliente, domo_reserva, domo_restaurante
from flask import render_template, request, url_for, redirect, session

db = models.db

@app.route('/')
def index():

    form = RegisterForm()
    
    return render_template("home.html")

@app.route('/register', methods=['GET','POST'])
def register():

    form = RegisterForm()
    
    if request.method == 'POST':
        
        email = request.form.get('email')
        password = request.form.get('password')
        
        new_user = User(email = email, password = password)
        
        return new_user.email + " - " +new_user.estado+ " - " + str(new_user.password_hash)
    
    return render_template("assets/register.html", form = form)

#Caso de uso realizar reserva - Ernesto Opazo

@app.route('/reservar/<id>', methods=['GET','POST'])
def reservar(id):
    
    #session["cli_id"] = 1
    
    day_choice = [1,2,3]
    hour_choice = [1,2,3]
    
    form = ReservaForm()
    mesa_form = MesaForm()
    client_form = ClientForm()
    
    form.dia.choices = day_choice
    form.hora.choices = hour_choice
    
    restaurante = models.domo_restaurante.get_by_id(id)
    mesas = restaurante.get_mesas()
    
    for item in mesas:
        mesa_form.mesa.choices.append((item.msa_id, item.msa_numero))
    
    data = {
        "RESTAURANTE_ID": restaurante.rtr_id,
        "nombre": restaurante.rtr_nombre,
        "descripcion": restaurante.rtr_descripcion
    }
    
    
    return render_template("cli_reservar.html", data = data, form = form, mesa_form = mesa_form, client_form = client_form)

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
    
    return render_template("cli_reservar_not_registered.html", data = data, client_form = client_form)

@app.route('/reservar/<id_restaurante>/generar_reserva', methods=['GET','POST'])
def reserva_create(id_restaurante):
    
    if request.method == 'POST':
        
        hora = request.form['hora']
        fecha = request.form["dia"]
        mesa_id = request.form['mesa']
        estado = "CREADA"
        
        restaurante = domo_restaurante.get_by_id(id_restaurante)
        id_reserva = restaurante.generate_reserva(hora, fecha, mesa_id, estado)
        
        if session.get('cli_id') is None:
            return redirect(url_for('reserva_not_registered', id_restaurante = id_restaurante, id_reserva = id_reserva))
        
        reserva = domo_reserva.get_by_id(id_reserva)
        
        medio_de_pago = request.form["medio_de_pago"]
        
        dict_mdp = {
            "DEBITO": 1,
            "EFECTIVO": 2,
            "WEBPAY": 3
        }
        
        reserva.cli_id = session["cli_id"]
        reserva.tpg_id = dict_mdp[medio_de_pago] 
        
        if medio_de_pago is "WEBPAY":
            pass
        
        reserva.estado = "REALIZADA"
        db.session.commit()
        
        return redirect(url_for('reserva_exitosa', id_restaurante = id_restaurante, id_reserva = id_reserva))


@app.route('/reservar/<id_restaurante>/<id_reserva>/update_reserva', methods=['GET','POST'])
def reserva_update_new_client(id_restaurante, id_reserva):
    
    if request.method == 'POST':
        return     
    return    

@app.route('/reservar/<id_restaurante>/<id_reserva>/reserva_exitosa', methods=['GET','POST'])
def reserva_exitosa(id_restaurante, id_reserva):
    
    restaurante = models.domo_restaurante.get_by_id(id_restaurante)
    reserva = models.domo_reserva.get_by_id(id_reserva)
    
    return render_template("cli_ver_reservas.html")

@app.route('/cliente/ver_reservas', methods=['GET','POST'])
def cli_ver_reservas():
    
    return render_template("cli_ver_reservas.html")


@app.route('/restaurante/ver_reservas', methods=['GET','POST'])
def res_ver_reservas():
    
    return render_template("res_ver_reservas.html")

########- FIN DE CASO DE USO -#################

@app.route('/logout', methods=['GET','POST'])
def logout():
    
    session.clear()
    return redirect(url_for('index'))