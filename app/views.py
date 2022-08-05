from app import app
from app import models as db
from app.forms import RegisterForm, LoginForm
from app.models import User
from notifypy import Notify
from flask import render_template, request,session, redirect,url_for
from sqlalchemy import func
import bcrypt

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
    






@app.route('/register', methods=['GET','POST'])
def register():

    form = RegisterForm()
    
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        new_user = User(email = email, password = password)

        return new_user.email + " - " +new_user.estado+ " - " + str(new_user.password_hash)
    
    return render_template("assets/register.html", form = form)

@app.route('/login',methods=['GET','POST'])
def login():
    #session.clear
    notification=Notify()
    form = LoginForm()
    form.remember_me=True   
    if request.method == "POST":
        
        user = request.form.get('email')
        pw = request.form.get('password')
        #a="hola mundo"
        #rmb_me=request.form.get('remember_me')
        phashed= db.User.query.filter(db.email== user).first()

        if len(phashed.email)>0:
            if bcrypt.checkpw(pw, phashed.password_hash):
                print("Coinciden")
                session['nombre']= phashed['nombre']
                session['email']= phashed['email']
                session['tipo']=phashed['tipo']

                if session['tipo']==1:
                    return render_template("HOME/cl_home", tipo=session['tipo'])
                elif session['tipo']==2:
                    return render_template("HOME/res_home",tipo=session['tipo'])
                elif session['tipo'] ==3:
                    return render_template("HOME/adm_home",tipo=session['tipo'])

            else:
                print("No coinciden")
                notification.title= "Error de Acceso"
                notification.message="Correo o contraseña incorrecta"
                notification.send()
                return redirect(url_for('index.html'))
        else:
            notification.title= "Error de Acceso"
            notification.message="Usuario incorrecto"
            notification.send()
            return redirect(url_for('index.html'))

    return render_template("assets/login.html", form = form)

    