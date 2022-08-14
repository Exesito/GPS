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
    
    __tablename__ = 'domo_reserva'
    rsv_id = db.Column('rsv_id', db.Integer, primary_key = True)
    msa_id = db.Column('msa_id', db.Integer, db.ForeignKey('domo_mesa.msa_id'))
    tpg_id = db.Column('tpg_id', db.Integer, db.ForeignKey('domo_tipodepago.tpg_id'))
    rsv_hora = db.Column('rsv_hora', db.Time)
    rsv_fecha = db.Column('rsv_fecha', db.Date)
    rsv_asistencia = db.Column('rsv_asistencia', db.String(30))
    rsv_fechaderegistro = db.Column('rsv_fechaderegistro', db.Date)
    #Columna de id cliente
    #Columna de estatus Fail/Success
    
    def add_into_database(self):
        
        if(self.can_reserva): return False
        
        db.session.add(self)
        db.session.commit()
        
        return True
    
    def can_reserva(self):
        
        if (self.verify_fecha): return False
        if (self.verify_horario): return False
        
        return True
    
    def verify_fecha(self):
        
        if self.rsv_fechaderegistro > self.rsv_fecha: return False
        
        return True
    
    def verify_horario(self):
        
        pass
    
    @staticmethod
    def get_by_id(id):
        return Reserva.query.filter_by(rsv_id = id).first()

class domo_mesa(db.Model):
    __tablename__ = 'domo_mesa'
    rtr_id = db.Column('rtr_id', db.Integer, db.ForeignKey('domo_rtr.rtr_id'))
    msa_id = db.Column('msa_id', db.Integer, primary_key = true)
    msa_numero = db.Column('msa_numero', db.Integer)
    msa_capacidad = db.Column('msa_capacidad', db.Integer)
    msa_descripcion = db.Column('msa_descripcion', db.Text)