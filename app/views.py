from flask_security import LoginForm
from app import app, models
from app.forms import RegisterForm
from app.models import User
from flask import render_template, request,session, redirect,url_for
from sqlalchemy import func

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

    

@app.route('/ingresar_restaurante')
def ingresar_restaurante():

    return render_template("ingresar_restaurante.html")

@app.route('/ingresar_restaurante', methods=['POST'])
def ingresar_restaurante_post():
    if (request.method=='POST'):
        nombre = request.form['nombre']
        calle = request.form['calle']
        numero = request.form['numero']
        ciudad = request.form['ciudad']
        region = request.form['region']
        tipo_rest = request.form['tipo_rest']
        nombre_dueno = request.form['nombre_dueno']
        apellido_dueno = request.form['apellido_dueno']
        descripcion = request.form['descripcion']
        max_id = db.db.session.query(func.max(db.DOMO_DIRECCION.id)).scalar() + 1

        id_ciu = db.db.session.query(db.domo_ciudad.id).filter(db.DOMO_CIUDAD.nombre == ciudad).scalar()
        id_reg = db.db.session.query(db.domo_region.id).filter(db.DOMO_REGION.nombre == region).scalar()

        if (max_id == None):
            max_id = 1
        direccion = db.domo_direccion(id=max_id, ciu_id=id_ciu, dir_numerocalle=numero, dir_nombrecalle=calle) 

        db.db.session.add(direccion)
        db.session.commit()

        max_id = db.db.session.query(func.max(db.domo_restaurante.id)).scalar() + 1
        if(max_id == None):
            max_id = 1
        
        
        
        db.session.commit()
        return render_template("ingresar_restaurante.html")