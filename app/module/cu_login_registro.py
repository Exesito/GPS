from app import app
from app import models as db
#from os import path
from app.forms import EditForm1, EditForm2, EditForm3, IngresarRestaurante, RecoveryForm, ChangepasswordForm,RegisterForm, LoginForm, RegistroAdmin, RegistroEncargado
from app.models import domo_cliente, domo_direccion, domo_restaurante, domo_usuario

from notifypy import Notify
from flask import render_template, request,session, redirect,url_for
from sqlalchemy import func
import bcrypt

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/register', methods=['GET','POST'])
def register():

    form = RegisterForm()
    notification=Notify()
    ciudades = db.db.session.query(db.domo_ciudad.ciu_id, db.domo_ciudad.reg_id,db.domo_ciudad.ciu_nombre).all()
    regiones = db.db.session.query(db.domo_region.reg_id,db.domo_region.reg_nombre).all()
      
    if request.method == 'POST':
        
        email = request.form.get('email')
        password = request.form.get('password')
        confirm= request.form.get('confirm')
        nombre = request.form.get('nombre')
        apellido= request.form.get('apellido')
        rut= request.form.get('rut')
        celular= request.form.get('celular')
        region = request.form.get('regiones')
        print(region)
        ciudad = request.form.get(region)
        calle= request.form.get('calle')
        numero=request.form.get('numero')
        tipo= 1
        max_id_dir=0
        max_id_cli=0
        max_id_usr=0

        if db.db.session.query(db.domo_usuario).filter(db.domo_usuario.usr_login==email).first() == None :
            if (db.db.session.query(func.max(db.domo_direccion.dir_id)).scalar() == None):
              max_id_dir = 1
            else:
             max_id_dir = db.db.session.query(func.max(db.domo_direccion.dir_id)).scalar() + 1
            
            new_dir= db.domo_direccion(dir_id=max_id_dir, ciu_id=ciudad,dir_nombrecalle=calle,dir_numerocalle=numero)
            db.db.session.add(new_dir)
            db.db.session.commit()

            if (db.db.session.query(func.max(db.domo_usuario.usr_id)).scalar() == None):
                max_id_usr = 1
            else:
                 max_id_usr = db.db.session.query(func.max(db.domo_usuario.usr_id)).scalar() + 1

            new_user= db.domo_usuario(max_id_usr, tipo, email,password,"ACTIVA")
            db.db.session.add(new_user)
            db.db.session.commit()

            if (db.db.session.query(func.max(db.domo_cliente.cli_id)).scalar() == None):
                max_id_cli = 1
            else:
                max_id_cli = db.db.session.query(func.max(db.domo_cliente.cli_id)).scalar() + 1
        
            new_cli= db.domo_cliente(cli_id=max_id_cli,usr_id=max_id_usr,cli_nombre=nombre,cli_apellido=apellido,
                                      dir_id=max_id_dir,cli_telefono=celular,cli_rut=rut)
            db.db.session.add(new_cli)
            db.db.session.commit()

            notification.title= "Completado"
            notification.message="Usuario registrado con éxito"
            notification.send()
            return redirect(url_for('login'))
        else:
            notification.title= "Error"
            notification.message="Email ya existe"
            notification.send()
            return redirect(url_for("register"))
       # return new_user.email + " - " +new_user.estado+ " - " + str(new_user.password_hash)
    
    return render_template("cu_login_registro/register.html", form = form, regiones=regiones, ciudades=ciudades)

@app.route('/login',methods=['GET','POST'])
def login():
    #session.clear
    notification=Notify()
    form = LoginForm()
    #form.remember_me=True   
    if request.method == "POST":
        
        user = request.form.get('email')
        pw = request.form.get('password')
        #pw_hashed=bcrypt.hashpw(pw.encode('utf-8'),bcrypt.gensalt())
        
        #phashed= db.User.query.filter(db.email== user).first()
        usuario=db.domo_usuario.query.filter(db.domo_usuario.usr_login == user).first()

        if usuario != None:
            if bcrypt.checkpw(pw.encode('utf-8'), usuario.usr_contrasena.encode('utf-8')):
                print("Coinciden")
                
                #session['nombre']= phashed['nombre']
                session['user']= usuario.usr_login
                session['tipo']=usuario.tip_id

                if session['tipo']==1:
                    session['cli_id']= domo_cliente.get_by_usr_id(usuario.usr_id).cli_id #### LA RESERVA OCUPA ESTO ####
                    return redirect(url_for('dashboard'))
                
                elif session['tipo']==2:
                    session["rtr_id"] = db.db.session.query(db.domo_usuario, db.domo_encargadortr).filter(
                        db.domo_usuario.usr_id == db.domo_encargadortr.usr_id,
                        db.domo_usuario.usr_id == usuario.usr_id
                    ).first().domo_encargadortr.rtr_id
                    print(session["rtr_id"])
                    
                    return redirect(url_for('dashboard'))
                elif session['tipo'] ==3:
                    return redirect(url_for('dashboard'))

            else:
                print("No coinciden")
                notification.title= "Error de Acceso"
                notification.message="Correo o contraseña incorrecta"
                notification.send()
               # dir_absoluta=path.abspath(path.dirname(__file__))
               # notification.icon = path.join(dir_absoluta,".GPS/app/static/icon.png")
               #print("A",path.join(dir_absoluta,icono))
                return redirect(url_for("login"))
        else:
            notification.title= "Error de Acceso"
            notification.message="Usuario incorrecto"
            notification.send()
            return redirect(url_for("login"))

    return render_template("cu_login_registro/login.html", form = form)

@app.route('/dashboard')
def dashboard():
    user= session['user']
    usuario=session['tipo']
    return render_template("HOME/user_home.html")

#@app.route('/recuperar_contrasena')
#def recuperar_contrasena():
#    form = RecoveryForm()
#    notification=Notify()

#@app.route('/cambio_contrasena')
#def cambio_contrasena():
#    form= ChangepasswordForm()
#    notification=Notify()

