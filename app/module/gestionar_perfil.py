from app import app
from app import models as db
import unittest

from flask import render_template, request,session, redirect,url_for
from sqlalchemy import func

@app.route('/perfil<login>')
def perfil(login):

    usuario = db.domo_usuario.query.filter_by(usr_login=login).first()
    cliente = db.db.session.query(db.domo_cliente,db.domo_usuario,db.domo_direccion,db.domo_ciudad,db.domo_region).filter(db.domo_usuario.usr_id==usuario.usr_id,
                                db.domo_cliente.usr_id==usuario.usr_id,db.domo_cliente.dir_id==db.domo_direccion.dir_id,
                            db.domo_direccion.ciu_id==db.domo_ciudad.ciu_id,db.domo_ciudad.reg_id==db.domo_region.reg_id).first()

    return render_template("gestionar perfil/editar_perfil.html",cliente=cliente)

@app.route('/perfil/actualizar_perfil/<id>')
def actualizar_perfil(id):

    cliente = db.db.session.query(db.domo_cliente,db.domo_direccion,db.domo_ciudad,db.domo_region).filter(db.domo_usuario.usr_id==id,
                                db.domo_cliente.usr_id==db.domo_usuario.usr_id,db.domo_direccion.dir_id==db.domo_cliente.dir_id,
                                db.domo_direccion.ciu_id==db.domo_ciudad.ciu_id,
                                db.domo_ciudad.reg_id==db.domo_region.reg_id).first()

    ciudades = db.db.session.query(db.domo_ciudad).all()
    regiones = db.db.session.query(db.domo_region).all()
    return render_template("gestionar perfil/actualizar_perfil.html",cliente=cliente,ciudades=ciudades,regiones=regiones)


@app.route('/actualizar_perfil/<id>', methods=['POST'])
def subir_nuevo_perfil(id):
    
    if request.method == 'POST':
        usr = db.db.session.query(db.domo_usuario).filter(db.domo_cliente.cli_id==id,db.domo_usuario.usr_id==db.domo_cliente.usr_id).first()
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