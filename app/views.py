from flask_security import LoginForm
from app import app
from app import models as db
from app.forms import RegisterForm
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
    session.clear
    notification=Notify()

    form=LoginForm()
    form.remember_me=True
    if request.method == "POST":

        user = request.form.get('email')
        pw = request.form.get('password')
        rmb_me=request.form.get('remember_me')
        phashed= db.User.query.filter(db.email== user).first()

        if len(phashed.email)>0:
            if bcrypt.checkpw(pw, phashed.password_hash):
                print("Coinciden")
                session['nombre']= phashed['nombre']
                session['email']= phashed['email']
                session['tipo']=phashed['tipo']

                if session['tipo']==1:
                    return render_template("HOME/cl_home")
                elif session['tipo']==2:
                    return render_template("HOME/res_home")
                elif session['tipo'] ==3:
                    return render_template("HOME/adm_home")


            else:
                print("No coinciden")
                notification.title= "Error de Acceso"
                notification.message="Correo o contraseña incorrecta"
                notification.send()
        
        else:
            notification.title= "Error de Acceso"
            notification.message="Usuario incorrecto"
            notification.send()
            return redirect(url_for('index.html'))

    return render_template("assets/login.html", form = form)

    

@app.route('/ingresar_restaurante')
def ingresar_restaurante():

    return render_template("assets/ingresar_restaurante.html")

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
        tipo_rest=1

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
            max_id = db.db.session.query(func.max(db.domo_restaurante.id)).scalar() + 1
        
        new_rest = db.domo_restaurante(rtr_id=max_id, rtr_nombre=nombre, rtr_descripcion=descripcion, 
                                        rtr_tipo=tipo_rest, rtr_nombredueno=nombre_dueno, 
                                        rtr_apellidodueno=apellido_dueno, dir_id=max_id_dir)
        
        db.db.session.add(new_rest)
        db.db.session.commit()
        return render_template("ingresar_restaurante.html")