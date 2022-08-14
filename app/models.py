from flask_sqlalchemy import SQLAlchemy
import json
from flask_security import Security, SQLAlchemyUserDatastore, UserMixin
import bcrypt

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password_hash = db.Column(db.String(128))

    @property
    def password(self):
        raise AttributeError('password not readable')
    @password.setter
    def password(self, password):
        self.password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        print(self.password_hash)
        
    def verify_password(self, password):
        return bcrypt.checkpw(password, self.password_hash)
    
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.tip_id = 1 #Tipo de Usuario Cliente
        self.estado = 'ACTIVO'
        
        #db.session.commit()

class Reserva(db.Model):
    
    pass