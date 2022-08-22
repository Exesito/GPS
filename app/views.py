from app import app, models
from app.forms import RegisterForm, ReservaForm, MesaForm, ClientForm
from app.models import User, domo_cliente, domo_reserva, domo_restaurante
from flask import render_template, request, url_for, redirect, session
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


@app.route('/logout', methods=['GET','POST'])
def logout():
    
    session.clear()
    return redirect(url_for('index'))