from app import app, models as db
from flask import render_template, request, session, redirect,url_for




@app.route('/editor_cartas',methods=['GET','POST'])
def editor_cartas():
    session['email'] = 'P5W512FM N3REWJ0IEN9'  #Linea para establecer un usuario mientras no hayan sesiones
    
    email = session["email"]    
    if request.method =='POST':
        
        file = request.files.get('file')
        nombre = request.form['nombre']
        print(file)

    cartas = db.db.session.query(db.domo_carta, db.domo_restaurante, db.domo_encargadortr, db.domo_usuario).filter(
        db.domo_usuario.usr_login == email,
        db.domo_encargadortr.usr_id == db.domo_usuario.usr_id,
        db.domo_restaurante.rtr_id == db.domo_encargadortr.rtr_id,
        db.domo_carta.rtr_id == db.domo_restaurante.rtr_id
    ).all()

    lista_rtr,rtr_names = [], []
    for carta in cartas:
        if not lista_rtr.__contains__(carta.domo_restaurante.rtr_nombre):
            lista_rtr.append(carta.domo_restaurante.rtr_nombre)
        if not rtr_names.__contains__(carta.domo_restaurante.rtr_nombre):
            string = str(carta.domo_restaurante.rtr_id) + " " +  carta.domo_restaurante.rtr_nombre
            
            rtr_names.append(string)
    
    return render_template("CRUD-Horarios/editor_carta.html", lista_rtr = lista_rtr, lista_cartas = cartas, rtr_names = rtr_names)

