from app import app, models as db
from flask import render_template, request, session, redirect,url_for

import os
from werkzeug.utils import secure_filename
from sqlalchemy import func


@app.route('/editor_cartas',methods=['GET','POST'])
def editor_cartas():
    email = session["user"]    
    if request.method =='POST':
        
        file = request.files
        print('archivo recibido: ', file)
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        

        

    cartas = db.db.session.query(db.domo_carta, db.domo_restaurante, db.domo_encargadortr, db.domo_usuario).filter(
        db.domo_usuario.usr_login == email,
        db.domo_encargadortr.usr_id == db.domo_usuario.usr_id,
        db.domo_restaurante.rtr_id == db.domo_encargadortr.rtr_id,
        db.domo_carta.rtr_id == db.domo_restaurante.rtr_id
    ).all()

    rtr_names = []
    for rtr in cartas:
        if not rtr_names.__contains__(rtr.domo_restaurante.rtr_nombre):
            string = str(rtr.domo_restaurante.rtr_id) + "-" +  rtr.domo_restaurante.rtr_nombre
            
            rtr_names.append(string)
    result = [] 
    [result.append(x) for x in rtr_names if x not in result] 
    return render_template("CRUD-Horarios/editor_carta.html", lista_cartas = cartas, rtr_names = rtr_names)

@app.route('/nueva_carta/<car_id>',methods=['GET','POST'])
def nueva_carta(car_id):
    
    if request.method == 'POST':
        
        if 'file' not in request.files:
            print('No file part tho')
        file = request.files['new_carta']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            print('No selected file')
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('editor_cartas'))

    return render_template("CRUD-Horarios/agregar_carta.html")

@app.route('/editor_cartas/add<rtr_names>',methods=['GET','POST'])
def add_carta(rtr_names):
    if request.method == 'POST':
        if 'file' not in request.files:
            print('No file part')
        file = request.files['new_carta']
        if file.filename == '':
            print('No selected file')
        if file:
            id = db.db.session.query(func.max(db.domo_carta.car_id)).scalar() + 1
            filename = secure_filename('carta-' + str(id) + '.pdf')
            nombre = request.form['nombre_carta']
            nombre_rtr = request.form.get('nombre_rtr')
            
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            new_carta = db.domo_carta()
            return redirect(url_for('editor_cartas'))
    return render_template('/CRUD-Horarios/add_carta.html', rtr_names = rtr_names)

@app.route('/editor_cartas/del', methods=['GET','POST'])
def del_carta():
    if request.method =='POST':
        id = request.json['id']
        print("request para borrar", id)
        db.db.session.query(db.domo_carta).filter(db.domo_carta.car_id == id).delete()
        db.db.session.commit()
    return redirect(url_for('editor_cartas'))