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

    return render_template("crud_usuario/adm_editar_usuario.html", usuario=usuario,usuarios=usuarios, form=form)