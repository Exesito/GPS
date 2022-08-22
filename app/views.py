from asyncio.windows_events import NULL
from app import app
from app import models as db
#from os import path
from app.forms import EditForm1, EditForm2, EditForm3, IngresarRestaurante, RecoveryForm, ChangepasswordForm,RegisterForm, LoginForm, RegistroAdmin, RegistroEncargado


from notifypy import Notify
from flask import render_template, request,session, redirect,url_for
from sqlalchemy import func
import bcrypt

@app.route('/')
def index():

    return render_template("home.html")



