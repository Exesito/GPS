from app import app
from app import models as db

from app.forms import IngresarRestaurante
from flask import render_template, request,session, redirect,url_for
from sqlalchemy import func

@app.route('/ingresar_restaurante')
def ingresar_restaurante():

    tipo_restaurante=db.domo_tiporestaurante.query.all()
    ciudades = db.db.session.query(db.domo_ciudad.ciu_id,db.domo_ciudad.ciu_nombre,db.domo_ciudad.reg_id).all()
    regiones = db.db.session.query(db.domo_region.reg_id,db.domo_region.reg_nombre).all()

    return render_template("gestionar restaurantes/ingresar_restaurante.html", tipo_restaurante=tipo_restaurante,ciudades=ciudades,regiones=regiones)

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
        return render_template("gestionar restaurantes/ingresar_restaurante.html",tipo_restaurante=tipo_restaurante,ciudades=ciudades,regiones=regiones)

@app.route('/gestionar_restaurantes')
def gestionar_restaurantes():
    restaurantes = db.db.session.query(db.domo_restaurante, db.domo_direccion, db.domo_ciudad, db.domo_region, db.domo_tiporestaurante).filter(
                                        db.domo_restaurante.dir_id == db.domo_direccion.dir_id,
                                        db.domo_tiporestaurante.tpr_id == db.domo_restaurante.tpr_id,
                                        db.domo_direccion.ciu_id == db.domo_ciudad.ciu_id,
                                        db.domo_ciudad.reg_id==db.domo_region.reg_id).all()
    
    return render_template("gestionar restaurantes/gestionar_restaurantes.html", restaurantes=restaurantes)

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

    return render_template("gestionar restaurantes/editar_restaurante.html", restaurante=restaurante,ciudades=ciudades,regiones=regiones,tipo_restaurante=tipo_restaurante)


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

        return render_template("gestionar restaurantes/gestionar_restaurantes.html", restaurantes=restaurantes)

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


