from app import app, models
from app.forms import RegisterForm, ReservaForm, MesaForm, ClientForm
from app.forms import EditForm1, EditForm2, EditForm3, IngresarRestaurante, RecoveryForm, ChangepasswordForm,RegisterForm, LoginForm, RegistroAdmin, RegistroEncargado
from flask import render_template, request, url_for, redirect, session
from sqlalchemy import func
from app import models as db
from sqlalchemy import func

@app.route('/')
def index():
    return render_template("home.html")

