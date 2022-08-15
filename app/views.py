from app import app, models
from app.forms import RegisterForm
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
    
    data = {
        #"RESTAURANTE_ID": models.domo_restaurante.get_by_id(id),
        "RESTAURANTE_ID": 1
    }
    
    return render_template("reservar.html", data = data, registered = registered)

@app.route('/cliente/ver_reservas', methods=['GET','POST'])
def cli_ver_reservas():
    
    return render_template("cli_ver_reservas.html")


@app.route('/restaurante/ver_reservas', methods=['GET','POST'])
def res_ver_reservas():
    
    return render_template("res_ver_reservas.html")

########- FIN DE CASO DE USO -#################