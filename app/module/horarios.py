from app import app, models as db
from flask import render_template, request, session, redirect,url_for
from sqlalchemy import func

@app.route('/editor_horarios',methods=['GET','POST'])
def editor_horarios():

    email = session["user"]

    if request.method =='POST':
        
        nombre = request.json["nombre"]
        id = request.json["id"]
        apertura = request.json["apertura"]
        cierre = request.json["cierre"]
        dia_inicio = request.json["dia_inicio"]
        dia_fin = request.json["dia_fin"]
        rtr_id = request.json["rtr_id"]
        print("id del recién llegado: ", id, "\n")
        if(not id):
            id = db.db.session.query(func.max(db.domo_horario.hor_id)).scalar() + 1
            new_horario = db.domo_horario(hor_id=id, hor_nombre = nombre,
            rtr_id = rtr_id, hor_diainicio = dia_inicio, hor_diatermino = dia_fin,
            hor_horainicio = apertura, hor_horatermino = cierre, hor_activo = False)
            db.db.session.add(new_horario)
            db.db.session.commit()
        else:
            horario = db.db.session.query(db.domo_horario).filter(db.domo_horario.hor_id == id).first()
            horario.hor_nombre = nombre
            horario.hor_diainicio = dia_inicio
            horario.hor_diatermino = dia_fin
            horario.hor_horainicio = apertura
            horario.hor_horatermino = cierre
            db.db.session.commit()
        print( id, rtr_id, nombre, apertura, cierre, dia_inicio, dia_fin) # esta linea es para verificar que llegan los datos desde el frontend al backend a traves de ajax. Falta ingresar datos a bdd

    horarios = db.db.session.query(db.domo_horario, db.domo_encargadortr, db.domo_restaurante, db.domo_usuario).filter(
        db.domo_usuario.usr_login == email,
        db.domo_encargadortr.usr_id == db.domo_usuario.usr_id,
        db.domo_restaurante.rtr_id == db.domo_encargadortr.rtr_id,
        db.domo_horario.rtr_id == db.domo_restaurante.rtr_id
        ).all()
    rtr_names = []
    for rtr in horarios:
        if not rtr_names.__contains__(rtr.domo_restaurante.rtr_nombre):
            string = str(rtr.domo_restaurante.rtr_id) + "-" +  rtr.domo_restaurante.rtr_nombre
            
            rtr_names.append(string)
    result = [] 
    [result.append(x) for x in rtr_names if x not in result] 
    
    return render_template("CRUD-Horarios/editor_horario.html", horarios_count = zip(horarios, range(len(horarios))), isGestionable = True, rtr_names = result )

@app.route('/editor_horarios/del',methods=['POST'])
def editor_horarios_del():
    if request.method =='POST':
        id = request.json['id']
        print("request para borrar", id)
        db.db.session.query(db.domo_horario).filter(db.domo_horario.hor_id == id).delete()
        db.db.session.commit()
    return redirect(url_for('editor_horarios'))
