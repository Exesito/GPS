from app import app, models as db
from flask import render_template, request, session, redirect,url_for

@app.route('/editor_cartas',methods=['GET','POST'])
def editor_cartas():
    email = session["user"]    
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

    rtr_names = []
    for rtr in cartas:
        if not rtr_names.__contains__(rtr.domo_restaurante.rtr_nombre):
            string = str(rtr.domo_restaurante.rtr_id) + "-" +  rtr.domo_restaurante.rtr_nombre
            
            rtr_names.append(string)
    result = [] 
    [result.append(x) for x in rtr_names if x not in result] 
    return render_template("CRUD-Horarios/editor_carta.html", lista_cartas = cartas, rtr_names = rtr_names)

