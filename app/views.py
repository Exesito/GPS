#from flask_security import LoginForm
from app import app
from app import models as db
from app.forms import IngresarRestaurante, RegisterForm, LoginForm

from app.models import User, domo_restaurante
from notifypy import Notify
from flask import render_template, request,session, redirect,url_for
from sqlalchemy import func
import bcrypt

@app.route('/')
def index():

    return render_template("home.html")

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home.html'))

@app.route('/register', methods=['GET','POST'])
def register():

    form = RegisterForm()
    notification=Notify()
      
    if request.method == 'POST':
        
        email = request.form.get('email')
        password = request.form.get('password')
        #new_user = User(email = email, password = password)
        nombre = request.form.get('nombre')
        apellido= request.form.get('apellido')
        rut= request.form.get('rut')
        celular= request.form.get('celular')
        region=request.form.get('region')

        
        ciudad= request.form.get('ciudad')

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
                max_id_dir = 1
            else:
                 max_id_dir = db.db.session.query(func.max(db.domo_usuario.usr_id)).scalar() + 1

            new_user= db.domo_usuario(usr_id=max_id_usr, tip_id=tipo, usr_login=email,usr_contrasena=password
                                        ,usr_estado='ACTIVA')
            db.db.session.add(new_user)
            db.db.session.commit()

            if (db.db.session.query(func.max(db.domo_cliente.cli_id)).scalar() == None):
                max_id_dir = 1
            else:
                max_id_dir = db.db.session.query(func.max(db.domo_cliente.cli_id)).scalar() + 1
        
            new_cli= db.domo_cliente(cli_id=max_id_cli,usr_id=max_id_usr,cli_nombre=nombre,cli_apellido=apellido,
                                      dir_id=max_id_dir,cli_telefono=celular,cli_rut=rut, cli_tipo=tipo)
            db.db.session.add(new_cli)
            db.db.session.commit()

            notification.title= "Completado"
            notification.message="Usuario registrado con éxito"
            notification.send()
            return redirect(url_for('assets/register.html'),ciudades=ciudades)
        else:
            notification.title= "Error"
            notification.message="Email ya existe"
            notification.send()
            return redirect(url_for('assets/register.html'))
       # return new_user.email + " - " +new_user.estado+ " - " + str(new_user.password_hash)
    ciudades=db.db.session.query(db.domo_ciudad).all()
    regiones=db.db.session.query(db.domo_region).all()  
    return render_template("assets/register.html", form = form, regiones=regiones, ciudades=ciudades)

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
    ciudades = db.db.session.query(db.domo_ciudad.ciu_id,db.domo_ciudad.ciu_nombre,db.domo_ciudad.reg_id).all()
    regiones = db.db.session.query(db.domo_region.reg_id,db.domo_region.reg_nombre).all()

    return render_template("assets/ingresar_restaurante.html", tipo_restaurante=tipo_restaurante,ciudades=ciudades,regiones=regiones)

@app.route('/ingresar_restaurante', methods=['POST'])
def ingresar_restaurante_post():

    tipo_restaurante=db.domo_tiporestaurante.query.all()
    ciudades = db.db.session.query(db.domo_ciudad.ciu_id,db.domo_ciudad.ciu_nombre).all()
    regiones = db.db.session.query(db.domo_region.reg_id,db.domo_region.reg_nombre).all()

    form = IngresarRestaurante()
    if (request.method=='POST'):
        nombre = request.form.get('nombre')
        calle = request.form.get('calle')
        numero = request.form.get('numero')
        region = request.form.get('region')
        ciudad = request.form.get(region)
        tipo_rest = request.form.get('tipo_rest')
        nombre_dueno = request.form.get('nombre_dueno')
        apellido_dueno = request.form.get('apellido_dueno')
        descripcion = request.form.get('descripcion')
        vegetariana = request.form.get('vegetariana')
        vegana = request.form.get('vegana')


        if (db.db.session.query(func.max(db.domo_direccion.dir_id)).scalar() == None):
            max_id_dir = 1
        else:
            max_id_dir = db.db.session.query(func.max(db.domo_direccion.dir_id)).scalar() + 1
        direccion = db.domo_direccion(dir_id=max_id_dir, ciu_id=ciudad, dir_numerocalle=numero, dir_nombrecalle=calle) 
        

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
        return render_template("assets/ingresar_restaurante.html",tipo_restaurante=tipo_restaurante,ciudades=ciudades,regiones=regiones)

@app.route('/gestionar_restaurantes')
def gestionar_restaurantes():
    restaurantes = db.db.session.query(db.domo_restaurante, db.domo_direccion, db.domo_ciudad, db.domo_region, db.domo_tiporestaurante).filter(
                                        db.domo_restaurante.dir_id == db.domo_direccion.dir_id,
                                        db.domo_tiporestaurante.tpr_id == db.domo_restaurante.tpr_id,
                                        db.domo_direccion.ciu_id == db.domo_ciudad.ciu_id,
                                        db.domo_ciudad.reg_id==db.domo_region.reg_id).all()
    
    return render_template("assets/gestionar_restaurantes.html", restaurantes=restaurantes)


@app.route('/gestionar_restaurates/editar/<id>')
def editar_template(id):

    restaurante = db.db.session.query(db.domo_restaurante, db.domo_direccion, db.domo_ciudad, db.domo_region, 
                                        db.domo_tiporestaurante).filter(db.domo_restaurante.rtr_id == id, 
                                        db.domo_restaurante.dir_id == db.domo_direccion.dir_id, 
                                        db.domo_direccion.ciu_id == db.domo_ciudad.ciu_id, 
                                        db.domo_ciudad.reg_id == db.domo_region.reg_id).first()

    ciudades = db.db.session.query(db.domo_ciudad.ciu_id,db.domo_ciudad.ciu_nombre,db.domo_ciudad.reg_id).all()
    regiones = db.db.session.query(db.domo_region.reg_id,db.domo_region.reg_nombre).all()
    tipo_restaurante = db.domo_tiporestaurante.query.all()

    return render_template("assets/editar_restaurante.html", restaurante=restaurante,ciudades=ciudades,regiones=regiones,tipo_restaurante=tipo_restaurante)


@app.route('/gestionar_restaurantes/<id>', methods=['POST'])
def actualizar_rest(id):
    
    if (request.method=='POST'):
        nombre = request.form.get('nombre')
        calle = request.form.get('calle')
        numero = request.form.get('numero')
        region = request.form.get('region')
        ciudad = request.form.get(region)
        tipo_rest = request.form.get('tipo_rest')
        nombre_dueno = request.form.get('nombre_dueno')
        apellido_dueno = request.form.get('apellido_dueno')
        descripcion = request.form.get('descripcion')
        vegetariana = request.form.get('vegetariana')
        vegana = request.form.get('vegana')


    
        restaurante = db.domo_restaurante.query.filter_by(rtr_id=id).first()
        
        direccion = db.domo_direccion.query.filter_by(dir_id=restaurante.dir_id).first()

        if(direccion.dir_numerocalle != numero and direccion.dir_nombrecalle != calle and direccion.ciu_id != ciudad):
            max_id = db.db.session.query(func.max(db.domo_direccion.dir_id)).scalar() + 1
            new_direccion = db.domo_direccion(dir_id=max_id, ciu_id=ciudad, dir_numerocalle=numero, dir_nombrecalle=calle)
            db.db.session.add(new_direccion)
            db.db.session.commit()
            restaurante.dir_id = max_id


        restaurante.tpr_id = tipo_rest
        restaurante.rtr_nombre = nombre
        restaurante.rtr_rutacarta = "xd"
        restaurante.rtr_descripcion = descripcion

        if(vegetariana == "true"):
            vege = True
        else:
            vege = False
        
        restaurante.rtr_opvege = vege
        if(vegana == "true"):
            vega = True
        else:
            vega = False

        restaurante.rtr_opvega = vega
        restaurante.rtr_duenonombre = nombre_dueno
        restaurante.rtr_duenoapellido = apellido_dueno
        db.db.session.commit()

        restaurantes = db.db.session.query(db.domo_restaurante, db.domo_direccion, db.domo_ciudad, db.domo_region, db.domo_tiporestaurante).filter(
                                        db.domo_restaurante.dir_id == db.domo_direccion.dir_id,
                                        db.domo_tiporestaurante.tpr_id == db.domo_restaurante.tpr_id,
                                        db.domo_direccion.ciu_id == db.domo_ciudad.ciu_id,
                                        db.domo_ciudad.reg_id==db.domo_region.reg_id).all()

        return render_template("assets/gestionar_restaurantes.html", restaurantes=restaurantes)

