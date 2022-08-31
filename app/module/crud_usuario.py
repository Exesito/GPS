from app import app
from app import models as db
#from os import path
from app.forms import EditForm1, EditForm2, EditForm3, IngresarRestaurante, RecoveryForm, ChangepasswordForm,RegisterForm, LoginForm, RegistroAdmin, RegistroEncargado
from app.models import domo_cliente, domo_direccion, domo_restaurante, domo_usuario

from notifypy import Notify
from flask import render_template, request,session, redirect,url_for
from sqlalchemy import func
import bcrypt


@app.route('/gestionar_usuarios_admin')
def gestionar_usuarios_admin():
    usuarios = db.db.session.query(db.domo_usuario.usr_id,db.domo_usuario.usr_login,db.domo_usuario.tip_id,db.domo_usuario.usr_estado).all()
      
    return render_template("crud_usuario/adm_gestionar_usuarios.html", usuarios=usuarios)

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
        restaurante=request.form.get('restaurante')
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
        
            new_enc= db.domo_encargadortr(enc_id=max_id_enc,usr_id=max_id_usr,rtr_id=restaurante,enc_nombre=nombre,enc_apellido=apellido,
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
        
    return render_template("crud_usuario/adm_ingresar_usuario_encargado.html", form = form, restaurantes=restaurantes)

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
            
    return render_template("crud_usuario/adm_ingresar_usuario.html", form = form)

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
        if usuario.usr_id!=0: #usuario admin de admins
            if usuario.usr_login!=session['user'] :
                db.db.session.delete(usuario)
                db.db.session.commit()
            else:
                print("No se puede borrar al usuario Admin en uso")
            
        else:
            print("No se borra el usuario Super Admin")

        
    return redirect(url_for('gestionar_usuarios_admin'))


    
@app.route('/gesionar_usuarios_admin/editar1/<id>',methods=['GET','POST'])
def actualizar_usuario1(id):
    notification=Notify()
    usuario= db.db.session.query(db.domo_usuario).filter(db.domo_usuario.usr_id==id).first()
    form=EditForm1()
    cliente=db.domo_cliente.query.filter_by(usr_id=usuario.usr_id).first()
    #direccion1=db.domo_direccion.query.filter_by(dir_id=cliente.dir_id).first()
    direccion1 = db.db.session.query(db.domo_direccion, db.domo_ciudad, db.domo_region).filter(db.domo_direccion.dir_id==cliente.dir_id, 
                                        db.domo_direccion.ciu_id == db.domo_ciudad.ciu_id, 
                                        db.domo_ciudad.reg_id == db.domo_region.reg_id).first()
    ciudades = db.db.session.query(db.domo_ciudad.ciu_id, db.domo_ciudad.reg_id,db.domo_ciudad.ciu_nombre).all()
    regiones = db.db.session.query(db.domo_region.reg_id,db.domo_region.reg_nombre).all()

    if (request.method=='POST'):    
        if usuario.tip_id==1:
            email=request.form.get('email')
            contrasena=request.form.get('contrasena')
            estado=request.form.get('estado')
            nombre = request.form.get('nombre')
            apellido=request.form.get('apellido')
            rut=request.form.get('rut')
            celular=request.form.get('celular')
            calle = request.form.get('calle')
            numero = request.form.get('numero')
            region = request.form.get('regiones')
            ciudad = request.form.get(region)

            direccion1.domo_direccion.dir_nombrecalle=calle
            direccion1.domo_direccion.dir_numerocalle=numero
            direccion1.domo_direccion.ciu_id=ciudad
            
            if (email!=None) and (email!=""):
                if db.db.session.query(db.domo_usuario).filter(db.domo_usuario.usr_login==email).first() == None :
                    usuario.usr_login = email
                else:
                    
                    notification.title= "Error"
                    notification.message="Email ya en uso"
                    notification.send()
                    return redirect(url_for("gestionar_usuarios_admin"))

            if (contrasena!=None)and (contrasena!=""):
                pw = bcrypt.hashpw(contrasena.encode('utf-8'), bcrypt.gensalt())
                usuario.usr_contrasena=pw.decode('utf-8')

            if estado!="":
                usuario.usr_estado=estado
            if nombre!="":
                cliente.cli_nombre = nombre
            if apellido!="":    
                cliente.cli_apellido = apellido
            if rut!="":
                cliente.cli_rut = rut
            if celular!="":
                cliente.cli_telefono=celular

            db.db.session.commit()
    return render_template("crud_usuario/adm_editar_usuario_cli.html", usuario=usuario, cliente=cliente , regiones=regiones, ciudades=ciudades, form = form, direccion=direccion1)

@app.route('/gesionar_usuarios_admin/editar2/<id>',methods=['GET','POST'])
def actualizar_usuario2(id):
    usuario= db.db.session.query(db.domo_usuario).filter(db.domo_usuario.usr_id==id).first()
    restaurantes=db.db.session.query(db.domo_restaurante.rtr_id,db.domo_restaurante.rtr_nombre).all()
    form=EditForm2()
    notification=Notify()
    encargado=db.domo_encargadortr.query.filter_by(usr_id=usuario.usr_id).first()
    
    if (request.method=='POST' ):  
        if usuario.tip_id==2:
            email=request.form.get('email')
            contrasena=request.form.get('contrasena')
            estado=request.form.get('estado')
            nombre=request.form.get('nombre')
            apellido=request.form.get('apellido')
            rut=request.form.get('rut')
            restaurante=request.form.get('restaurante')

            
            if (email!=None) and (email!=""):
                if db.db.session.query(db.domo_usuario).filter(db.domo_usuario.usr_login==email).first() == None :
                    usuario.usr_login = email
                else:
                    
                    notification.title= "Error"
                    notification.message="Email ya en uso"
                    notification.send()
                    return redirect(url_for("gestionar_usuarios_admin"))
                    
            if (estado!=None) and (estado!=""):
                usuario.usr_estado=estado

            if (nombre!=None) and (nombre!=""):
                encargado.enc_nombre=nombre
            
            if (apellido!=None) and (apellido!=""):
                encargado.enc_apellido=apellido

            if (rut!=None) and (rut!=""):
                encargado.enc_rut=rut
            
            if (restaurante!=None) and (restaurante!=""):
                encargado.rtr_id=restaurante


            if (contrasena!=None)and (contrasena!=""):
                hash=bcrypt.hashpw(contrasena.encode('utf-8'),bcrypt.gensalt())
                usuario.usr_contrasena=hash.decode('utf-8')
            
            
            db.db.session.commit()

    return render_template("crud_usuario/adm_editar_usuario_enc.html", usuario=usuario, encargado=encargado ,restaurantes=restaurantes, form = form)

@app.route('/gesionar_usuarios_admin/editar3/<id>',methods=['GET','POST'])
def actualizar_usuario3(id):
    usuario= db.db.session.query(db.domo_usuario).filter(db.domo_usuario.usr_id==id).first()
    form=EditForm3()
    notification=Notify()
    if (request.method=='POST'):
        if usuario.tip_id==3:
            email=request.form.get('email')
            contrasena=request.form.get('contrasena')
            estado=request.form.get('estado')

            if (email!=None) and (email!=""):
                if db.db.session.query(db.domo_usuario).filter(db.domo_usuario.usr_login==email).first() == None :
                    if usuario.usr_id!=0: #usuario admin de admins                    
                        if usuario.usr_login!=session['user'] :
                            usuario.usr_login = email
                        else:
                            print("No se puede editar el correo del usuario Admin en uso")
                    else:
                        print ("No se puede cambiar el correo del usuario Super Admin")
                else:
                    
                    notification.title= "Error"
                    notification.message="Email ya en uso"
                    notification.send()
                    return redirect(url_for("gestionar_usuarios_admin"))

            if (contrasena!=None)and (contrasena!=""):
                hash=bcrypt.hashpw(contrasena.encode('utf-8'),bcrypt.gensalt())
                usuario.usr_contrasena=hash.decode('utf-8')

            if (estado!=None) and (estado!=""):
                usuario.usr_estado=estado

            db.db.session.commit()

        db.db.session.commit()
    return render_template("crud_usuario/adm_editar_usuario.html", usuario=usuario, form = form)