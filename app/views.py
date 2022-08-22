from asyncio.windows_events import NULL
from app import app
from app import models as db
#from os import path
from app.forms import EditForm1, EditForm2, EditForm3, IngresarRestaurante, RecoveryForm, ChangepasswordForm,RegisterForm, LoginForm, RegistroAdmin, RegistroEncargado


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
    
    return render_template("assets/register.html", form = form, regiones=regiones, ciudades=ciudades)

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
                    return redirect(url_for('dashboard'))
                elif session['tipo']==2:
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

    return render_template("assets/login.html", form = form)

@app.route('/dashboard')
def dashboard():
    user= session['user']
    usuario=session['tipo']
    return render_template("HOME/user_home.html")

@app.route('/recuperar_contrasena')
def recuperar_contrasena():
    form = RecoveryForm()
    notification=Notify()

@app.route('/cambio_contrasena')
def cambio_contrasena():
    form= ChangepasswordForm()
    notification=Notify()

@app.route('/gestionar_usuarios_admin')
def gestionar_usuarios_admin():
    usuarios = db.db.session.query(db.domo_usuario.usr_id,db.domo_usuario.usr_login,db.domo_usuario.tip_id,db.domo_usuario.usr_estado).all()
      
    return render_template("assets/adm_gestionar_usuarios.html", usuarios=usuarios)

@app.route('/ingresar_usuario_encargado',methods=['GET','POST'])
def ingresar_usuario_encargado():
    form=RegistroEncargado()
    notification=Notify()
    restaurantes=db.db.session.query(db.domo_restaurante.rtr_id,db.domo_restaurante.rtr_nombre).all()

    if request.method=='POST':
        email= request.form.get('email')
        password = request.form.get('password')
        confirm=request.form.get('confirm')
        nombre=request.form.get('nombre')
        apellido=request.form.get('apellido')
        rut=request.form.get('rut')
        restaurant=request.form.get('restaurante')
        tipo=2
        max_id_enc=0
        max_id_usr=0

        if db.db.session.query(db.domo_usuario).filter(db.domo_usuario.usr_login==email).first() == None :

            if (db.db.session.query(func.max(db.domo_usuario.usr_id)).scalar() == None):
                max_id_usr = 1
            else:
                 max_id_usr = db.db.session.query(func.max(db.domo_usuario.usr_id)).scalar() + 1

            new_user= db.domo_usuario(max_id_usr, tipo, email,password,"ACTIVA")
            db.db.session.add(new_user)
            db.db.session.commit()

            if (db.db.session.query(func.max(db.domo_encargadortr.enc_id)).scalar() == None):
                max_id_enc = 1
            else:
                max_id_enc = db.db.session.query(func.max(db.domo_encargadortr.enc_id)).scalar() + 1
        
            new_enc= db.domo_encargadortr(enc_id=max_id_enc,usr_id=max_id_usr,rtr_id=restaurant,enc_nombre=nombre,enc_apellido=apellido,
                                      enc_rut=rut)
            db.db.session.add(new_enc)
            db.db.session.commit()

            notification.title= "Completado"
            notification.message="Usuario encargado ingresado con éxito"
            notification.send()
            return redirect(url_for('ingresar_usuario_encargado'))
        else:
            notification.title= "Error"
            notification.message="Email ya en uso"
            notification.send()
            return redirect(url_for("ingresar_usuario_encargado"))
        
    return render_template("assets/adm_ingresar_usuario_encargado.html", form = form, restaurantes=restaurantes)

@app.route('/ingresar_usuario_admin',methods=['GET','POST'])
def ingresar_usuario_admin():
    form= RegistroAdmin()
    notification=Notify()

    if request.method =='POST':
        email = request.form.get('email')
        password = request.form.get('password')
        confirm= request.form.get('confirm')
        tipo=3
        max_id_usr=0

        if db.db.session.query(db.domo_usuario).filter(db.domo_usuario.usr_login==email).first() == None :

            if (db.db.session.query(func.max(db.domo_usuario.usr_id)).scalar() == None):
                max_id_usr = 1
            else:
                 max_id_usr = db.db.session.query(func.max(db.domo_usuario.usr_id)).scalar() + 1

            new_user= db.domo_usuario(max_id_usr, tipo, email,password,"ACTIVA")
            db.db.session.add(new_user)
            db.db.session.commit()

            notification.title= "Completado"
            notification.message="Usuario Administrador ingresado con éxito"
            notification.send()
            return redirect(url_for('ingresar_usuario_admin'))
        else:
            notification.title= "Error"
            notification.message="Email ya en uso"
            notification.send()
            return redirect(url_for("ingresar_usuario_admin"))
            
    return render_template("assets/adm_ingresar_usuario.html", form = form)

@app.route('/gestionar_usuarios_admin<id>')
def eliminar_usuario(id):
    usuario = db.db.session.query(db.domo_usuario).filter(db.domo_usuario.usr_id==id).first()
    if usuario.tip_id==1:
        cliente=db.db.session.query(domo_cliente).filter(db.domo_cliente.usr_id==id).first()

        #direccion = db.domo_direccion.query.filter_by(dir_id=cliente.dir_id).first()
        #db.db.session.delete(direccion)
        #cliente.dir_id = 0
        #db.db.session.commit()

        db.db.session.delete(cliente)
        db.db.session.commit()

        db.db.session.delete(usuario)
        db.db.session.commit()

    elif usuario.tip_id==2:
        encargado=db.db.session.query(db.domo_encargadortr).filter(db.domo_encargadortr.usr_id==usuario.usr_id).first()
        db.db.session.delete(encargado)
        db.db.session.commit()
        db.db.session.delete(usuario)
        db.db.session.commit()

    elif usuario.tip_id==3:
        db.db.session.delete(usuario)
        db.db.session.commit()
        
    return redirect(url_for('gestionar_usuarios_admin'))

#@app.route('/gestionar_usuarios_admin/<id>')
#def editar_usuario(id):
#    usuario = db.db.session.query(db.domo_usuario).filter(db.domo_usuario.usr_id==id).first()
#    return render_template("assets/adm_editar_usuario.html", usuario=usuario)    

@app.route('/gestionar_usuarios_admin/editar/<id>', methods=['GET','POST'])
def actualizar_usuario(id):
    usuario = db.db.session.query(db.domo_usuario).filter(db.domo_usuario.usr_id==id).first()

    form=EditForm3()
    if (request.method=='POST'):
        
        if usuario.tip_id==1:
            form= EditForm1(obj=usuario)
            cliente=db.domo_cliente.query.filter_by(usr_id=usuario.usr_id).first
            direccion1=db.domo_direccion.query.filter_by(dir_id=cliente.dir_id).first
            ciudad1=db.domo_ciudad.query.filter_by(ciu_id=direccion1.ciu_id)

            form.email.data=usuario.usr_login
            email=request.form.get('email')

            contrasena=request.form.get('contrasena')

            form.estado.data=usuario.usr_estado
            estado=request.form.get('estado')

            form.nombre.data=cliente.cli_nombre
            nombre = request.form.get('nombre')

            form.apellido.data=cliente.cli_apellido
            apellido=request.form.get('nombre')

            form.rut.data=cliente.cli_rut
            rut=request.form.get('rut')

            form.celular.data=cliente.cli_telefono
            celular=request.form.get('celular')

            form.calle.data=direccion1.dir_nombrecalle
            calle = request.form.get('calle')

            form.numero.data=direccion1.dir_numerocalle
            numero = request.form.get('numero')

            form.region.data=ciudad1.reg_id
            region = request.form.get('region')

            form.ciudad.data=ciudad1.ciu_id
            ciudad = request.form.get(region)

            if(direccion1.dir_numerocalle != numero and direccion1.dir_nombrecalle != calle and direccion1.ciu_id != ciudad):
                max_id = db.db.session.query(func.max(db.domo_direccion.dir_id)).scalar() + 1
                new_direccion = db.domo_direccion(dir_id=max_id, ciu_id=ciudad, dir_numerocalle=numero, dir_nombrecalle=calle)
                db.db.session.add(new_direccion)
                db.db.session.commit()
                cliente.dir_id = max_id
            
            usuario.usr_login = email

            if len(contrasena)>0:
                hash=bcrypt.hashpw(contrasena.encode('utf-8'),bcrypt.gensalt())
                usuario.usr_contrasena=hash.decode('utf-8')

            usuario.usr_estado=estado

            cliente.cli_nombre = nombre
            cliente.cli_apellido = apellido
            cliente.cli_rut = rut
            cliente.cli_telefono=celular

            db.db.session.commit()

        if usuario.tip_id==2:

            form=EditForm2(obj=usuario)
            
            encargado=db.db.session.query(db.domo_encargadortr).filter(db.domo_encargadortr.usr_id==usuario.usr_id).first()

            form.estado.data=usuario.usr_estado
            email=request.form.get('email')

            form.estado.data=usuario.usr_estado
            contrasena=request.form.get('contrasena')

            form.estado.data=usuario.usr_estado
            estado=request.form.get('estado')

            form.estado.data=usuario.usr_estado
            nombre=request.form.get('nombre')

            form.estado.data=usuario.usr_estado
            apellido=request.form.get('apellido')

            form.estado.data=usuario.usr_estado
            rut=request.form.get('rut')

            usuario.usr_login = email

            if len(contrasena)>0:
                hash=bcrypt.hashpw(contrasena.encode('utf-8'),bcrypt.gensalt())
                usuario.usr_contrasena=hash.decode('utf-8')

            usuario.usr_estado=estado

            encargado.enc_nombre=nombre
            encargado.enc_apellido=apellido
            encargado.enc_rut=rut
            db.db.session.commit()

        if usuario.tip_id==3:
            form=EditForm3(obj=usuario)

            form.estado.data=usuario.usr_estado
            email=request.form.get('email')

            form.estado.data=usuario.usr_estado
            contrasena=request.form.get('contrasena')

            form.estado.data=usuario.usr_estado
            estado=request.form.get('estado')

            usuario.usr_login = email

            if len(contrasena)>0:
                hash=bcrypt.hashpw(contrasena.encode('utf-8'),bcrypt.gensalt())
                usuario.usr_contrasena=hash.decode('utf-8')

            usuario.usr_estado=estado
            db.db.session.commit()

        db.db.session.commit()

    usuarios = db.db.session.query(db.domo_usuario.usr_id,db.domo_usuario.usr_login,db.domo_usuario.tip_id,db.domo_usuario.usr_estado).all()

    return render_template("assets/adm_editar_usuario.html", usuario=usuario,usuarios=usuarios, form=form)





