#from flask_security import LoginForm
from app import app
from app import models as db
from app.forms import RegisterForm, LoginForm
from app.models import User
from notifypy import Notify
from flask import render_template, request,session, redirect,url_for
from sqlalchemy import func
import bcrypt

@app.route('/')
def index():

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

@app.route('/login',methods=['GET','POST'])
def login():
    #session.clear
    notification=Notify()
    form = LoginForm()
    form.remember_me=True   
    if request.method == "POST":
        
        user = request.form.get('email')
        pw = request.form.get('password')
        #a="hola mundo"
        #rmb_me=request.form.get('remember_me')
        phashed= db.User.query.filter(db.email== user).first()

        if len(phashed.email)>0:
            if bcrypt.checkpw(pw, phashed.password_hash):
                print("Coinciden")
                session['nombre']= phashed['nombre']
                session['email']= phashed['email']
                session['tipo']=phashed['tipo']

                if session['tipo']==1:
                    return render_template("HOME/cl_home", tipo=session['tipo'])
                elif session['tipo']==2:
                    return render_template("HOME/res_home",tipo=session['tipo'])
                elif session['tipo'] ==3:
                    return render_template("HOME/adm_home",tipo=session['tipo'])

            else:
                print("No coinciden")
                notification.title= "Error de Acceso"
                notification.message="Correo o contraseña incorrecta"
                notification.send()
                return redirect(url_for('index.html'))
        else:
            notification.title= "Error de Acceso"
            notification.message="Usuario incorrecto"
            notification.send()
            return redirect(url_for('index.html'))

    return render_template("assets/login.html", form = form)

    

@app.route('/ingresar_restaurante')
def ingresar_restaurante():

    tipo_restaurante=db.domo_tiporestaurante.query.all()

    return render_template("assets/ingresar_restaurante.html", tipo_restaurante=tipo_restaurante)

@app.route('/ingresar_restaurante', methods=['POST'])
def ingresar_restaurante_post():
    if (request.method=='POST'):
        nombre = request.form['nombre']
        calle = request.form['calle']
        numero = request.form['numero']
        ciudad = request.form['ciudad']
        region = request.form['region']
        tipo_rest = request.form['tipo_rest']
        nombre_dueno = request.form['nombre_dueno']
        apellido_dueno = request.form['apellido_dueno']
        descripcion = request.form['descripcion']
        vegetariana = request.form['vegetariana']
        vegana = request.form['vegana']

        id_ciu = db.db.session.query(db.domo_ciudad.ciu_id).filter(db.domo_ciudad.ciu_nombre == ciudad).scalar()
        id_reg = db.db.session.query(db.domo_region.reg_id).filter(db.domo_region.reg_nombre == region).scalar()

        if (db.db.session.query(func.max(db.domo_direccion.dir_id)).scalar() == None):
            max_id_dir = 1
        else:
            max_id_dir = db.db.session.query(func.max(db.domo_direccion.dir_id)).scalar() + 1
        direccion = db.domo_direccion(dir_id=max_id_dir, ciu_id=id_ciu, dir_numerocalle=numero, dir_nombrecalle=calle) 
        

        db.db.session.add(direccion)
        db.db.session.commit()

        if(db.db.session.query(func.max(db.domo_restaurante.rtr_id)).scalar() == None):
            max_id = 1
        else:
            max_id = db.db.session.query(func.max(db.domo_restaurante.rtr_id)).scalar() + 1

        if(vegetariana == "true"):
            vegetariana = True
        else:
            vegetariana = False

        if(vegana == "true"):
            vegana = True
        else:
            vegana = False
        
        new_rest = db.domo_restaurante(rtr_id=max_id,dir_id=max_id_dir,tpr_id=tipo_rest,
                                       rtr_nombre=nombre,rtr_rutacarta="xd",rtr_descripcion=descripcion, rtr_opvege=vegetariana, 
                                       rtr_opvega=vegana,rtr_duenonombre=nombre_dueno,rtr_duenoapellido=apellido_dueno)
        
        db.db.session.add(new_rest)
        db.db.session.commit()
        return render_template("assets/ingresar_restaurante.html")

@app.route('/gestionar_restaurantes')
def gestionar_restaurantes():
    restaurantes = db.db.session.query(db.domo_restaurante, db.domo_direccion, db.domo_ciudad, db.domo_region, db.domo_tiporestaurante).filter(
                                        db.domo_restaurante.dir_id == db.domo_direccion.dir_id,
                                        db.domo_tiporestaurante.tpr_id == db.domo_restaurante.tpr_id,
                                        db.domo_direccion.ciu_id == db.domo_ciudad.ciu_id,
                                        db.domo_ciudad.reg_id==db.domo_region.reg_id).all()
    
    print(restaurantes)
    return render_template("assets/gestionar_restaurantes.html", restaurantes=restaurantes)

@app.route('/gestionar_mesas')
def gestionar_mesas():
    mesas = db.db.session.query()
    return render_template("assets/gestionar_mesas.html", mesas=mesas)