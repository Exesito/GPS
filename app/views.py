from flask_security import LoginForm
from app import app, models
from app.forms import RegisterForm
from app.models import User
from flask import render_template, request,session, redirect,url_for

db = models.db

@app.route('/')
def index():

    form = RegisterForm()
    
    return render_template("home.html")

@app.route('/register', methods=['GET','POST'])
def register():

    form = RegisterForm()
    
    if request.method == 'POST':
        
        email = request.form.get('email')
        password = request.form.get('password')
        
        new_user = User(email = email, password = password)
        
        return new_user.email + " - " +new_user.estado+ " - " + str(new_user.password_hash)
    
    return render_template("assets/register.html", form = form)

def fetch_user(email):

    usuario = db.Usuario.query.filter(db.do == session['user']).first()
    if usuario.id_permiso == '2':
        usuario = db.Alumno.query.filter(db.Alumno.rut == usuario.login).first()
    elif usuario.id_permiso == '1':
        usuario = db.Apoderado.query.filter(db.Apoderado.rut == usuario.login).first()
    elif usuario.id_permiso == '3':
        usuario = db.Profesor.query.filter(db.Profesor.rut == usuario.rut).login()
    elif usuario.id_permiso == '4':
        usuario = db.Supervisor_Academico.query.filter(db.Supervisor_Academico.rut)
    return usuario


@app.route('/dashboard')
def dashboard():
    
    user = session['user']
    usuario = fetch_user(user)
    
    return render_template('dashboard.html', usuario = usuario)


@app.route('/login',methods=['GET','POST'])
def login():
    session.clear
    loginform=LoginForm()
    if request.method == "POST":

        user = db.Usuario.query.filter(db.Usuario.login == request.form.get("user")).first()
        pw = request.form.get("pass")

        if user and  user.contrasena == pw:
            session['user'] = user.login
            session['tipo_usuario'] = user.id_permiso
            

            colegio = db.Colegio.query.filter(db.Colegio.id == session["colegio"]).first()

            session['colegio_nombre'] = colegio.nombre

            return redirect(url_for('index'))

    return render_template('login.html')

    

