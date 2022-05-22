from app import app, models as db
from flask import render_template, session, url_for


@app.route('/')
def index():

    return render_template("home.html")

@app.route('/editor_horario')
def editor_horario():

    return(render_template('editor_horario.html'))

#Mi Restaurante
@app.route('/mi_restaurante')
def mi_restaurante():
    return render_template("mirestaurante.html")
    
