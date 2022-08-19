
from multiprocessing.connection import Client
from app import app, models
from app.forms import RegisterForm, ReservaForm, MesaForm, ClientForm
from app.models import User
from flask import render_template, request

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
    
    registered = 1
    
    day_choice = [1,2,3]
    hour_choice = [1,2,3]
    
    form = ReservaForm()
    mesa_form = MesaForm()

    form.dia.choices = day_choice
    form.hora.choices = hour_choice
    
    restaurante = models.domo_restaurante.get_by_id(id)
    mesas = restaurante.get_mesas()
    
    for item in mesas:
        mesa_form.mesa.choices.append((item.msa_id, item.msa_numero))
    
    data = {
        #"RESTAURANTE_ID": models.domo_restaurante.get_by_id(id),
        "RESTAURANTE_ID": restaurante.rtr_id,
        "nombre": restaurante.rtr_nombre,
        "descripcion": restaurante.rtr_descripcion
    }
    
    
    return render_template("cli_reservar.html", data = data, registered = registered, form = form, mesa_form = mesa_form)

@app.route('/reservar/<id_restaurante>/<id_reserva>/datos_cliente', methods=['GET','POST'])
def reserva_not_registered(id_restaurante, id_reserva):
    
    client_form = ClientForm()
    
    restaurante = models.domo_restaurante.get_by_id(id_restaurante)
    
    data = {
        #"RESTAURANTE_ID": models.domo_restaurante.get_by_id(id),
        "RESTAURANTE_ID": restaurante.rtr_id,
        "nombre": restaurante.rtr_nombre,
        "descripcion": restaurante.rtr_descripcion,
        "id_reserva": id_reserva
    }
    
    return render_template("cli_reservar_not_registered.html", data = data, client_form = client_form)

@app.route('/cliente/ver_reservas', methods=['GET','POST'])
def cli_ver_reservas():
    
    return render_template("cli_ver_reservas.html")


@app.route('/restaurante/ver_reservas', methods=['GET','POST'])
def res_ver_reservas():
    
    return render_template("res_ver_reservas.html")

########- FIN DE CASO DE USO -#################