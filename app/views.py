from asyncio.windows_events import NULL
from app import app
from app import models as db
#from os import path
from app.forms import EditForm1, EditForm2, EditForm3, IngresarRestaurante, RecoveryForm, ChangepasswordForm,RegisterForm, LoginForm, RegistroAdmin, RegistroEncargado
from app.models import domo_cliente, domo_direccion, domo_restaurante, domo_usuario

from notifypy import Notify
from flask import render_template, request,session, redirect,url_for
from sqlalchemy import func
import bcrypt

@app.route('/')
def index():

    return render_template("home.html")

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

@app.route('/gestionar_restaurantes<id>')
def eliminar_rest(id):
    print(id)
    restaurante = db.domo_restaurante.query.filter_by(rtr_id=id).first()
    direccion = db.domo_direccion.query.filter_by(dir_id=restaurante.dir_id).first()

    db.db.session.delete(direccion)
    restaurante.dir_id = None
    db.db.session.commit()

    db.db.session.delete(restaurante)
    db.db.session.commit()

    return redirect(url_for('gestionar_restaurantes'))


@app.route('/perfil<login>')
def perfil(login):

    usuario = db.domo_usuario.query.filter_by(usr_login=login).first()
    cliente = db.db.session.query(db.domo_cliente,db.domo_usuario,db.domo_direccion,db.domo_ciudad,db.domo_region).filter(db.domo_usuario.usr_id==usuario.usr_id,
                                db.domo_cliente.usr_id==usuario.usr_id,db.domo_cliente.dir_id==db.domo_direccion.dir_id,
                            db.domo_direccion.ciu_id==db.domo_ciudad.ciu_id,db.domo_ciudad.reg_id==db.domo_region.reg_id).first()

    return render_template("assets/editar_perfil.html",cliente=cliente)

@app.route('/perfil/actualizar_perfil/<id>')
def actualizar_perfil(id):

    cliente = db.db.session.query(db.domo_cliente,db.domo_direccion,db.domo_ciudad,db.domo_region).filter(db.domo_usuario.usr_id==id,
                                db.domo_cliente.usr_id==db.domo_usuario.usr_id,db.domo_direccion.dir_id==db.domo_cliente.dir_id,
                                db.domo_direccion.ciu_id==db.domo_ciudad.ciu_id,
                                db.domo_ciudad.reg_id==db.domo_region.reg_id).first()

    ciudades = db.db.session.query(db.domo_ciudad).all()
    regiones = db.db.session.query(db.domo_region).all()
    return render_template("assets/actualizar_perfil.html",cliente=cliente,ciudades=ciudades,regiones=regiones)


@app.route('/actualizar_perfil/<id>', methods=['POST'])
def subir_nuevo_perfil(id):
    
    if request.method == 'POST':
        usr = db.db.session.query(db.domo_usuario).filter(db.domo_cliente.cli_id==id,db.domo_usuario.usr_id==domo_cliente.usr_id).first()
        cliente=db.domo_cliente.query.filter_by(cli_id=id).first()

        numero = request.form.get('numero')
        calle = request.form.get('calle')
        region = request.form.get('region')
        ciudad = request.form.get(region)

        cliente.cli_nombre = request.form.get('nombre')
        cliente.cli_apellido = request.form.get('apellido')
        cliente.cli_telefono = request.form.get('telefono')
        
        direccion = db.domo_direccion.query.filter_by(dir_id=cliente.dir_id).first()

        if(direccion.dir_numerocalle != numero and direccion.dir_nombrecalle != calle and direccion.ciu_id != ciudad):
            max_id = db.db.session.query(func.max(db.domo_direccion.dir_id)).scalar() + 1
            new_direccion = db.domo_direccion(dir_id=max_id, ciu_id=ciudad, dir_numerocalle=numero, dir_nombrecalle=calle)
            db.db.session.add(new_direccion)
            db.db.session.commit()
            cliente.dir_id = max_id

        db.db.session.commit()
        return redirect(url_for('perfil',login=usr.usr_login))


@app.route('/perfil/eliminar_perfil<id>')
def eliminar_perfil(id):

    cliente = db.db.session.query(db.domo_cliente).filter(db.domo_cliente.cli_id==id).first()

    usuario = db.db.session.query(db.domo_usuario).filter(db.domo_cliente.cli_id==id,db.domo_cliente.usr_id==db.domo_usuario.usr_id).first()

    direccion = db.db.session.query(db.domo_direccion).filter(db.domo_cliente.cli_id==id,db.domo_cliente.dir_id==db.domo_direccion.dir_id).first()

    
    db.db.session.delete(cliente)
    db.db.session.delete(direccion)
    db.db.session.delete(usuario)
    db.db.session.commit()
 
    return redirect(url_for('logout'))