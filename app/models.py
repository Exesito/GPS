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
class domo_reserva(db.Model):
    
    __tablename__ = 'domo_reserva'
    rsv_id = db.Column('rsv_id', db.Integer, primary_key = True)
    msa_id = db.Column('msa_id', db.Integer, db.ForeignKey('domo_mesa.msa_id'))
    tpg_id = db.Column('tpg_id', db.Integer, db.ForeignKey('domo_tipodepago.tpg_id'))
    cli_id = db.Column('cli_id', db.Integer, db.ForeignKey('domo_cliente.cli_id'))
    rsv_hora = db.Column('rsv_hora', db.Time)
    rsv_fecha = db.Column('rsv_fecha', db.Date)
    rsv_asistencia = db.Column('rsv_asistencia', db.String(30))
    rsv_fechaderegistro = db.Column('rsv_fechaderegistro', db.Date)
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
        
        return True


    #Retorna todas las reservas del restaurante asociado
    def get_by_id_restaurante(id):

        query = domo_restaurante.query.join(domo_mesa).join(domo_reserva).filter(domo_restaurante.rtr_id == id).all()
        return query
    
    @staticmethod
    def get_by_id(id):
        return domo_reserva.query.filter_by(rsv_id = id).first()


class domo_mesa(db.Model):
    __tablename__ = 'domo_mesa'
    rtr_id = db.Column('rtr_id', db.Integer, db.ForeignKey('domo_rtr.rtr_id'))
    msa_id = db.Column('msa_id', db.Integer, primary_key = True)
    msa_numero = db.Column('msa_numero', db.Integer)
    msa_capacidad = db.Column('msa_capacidad', db.Integer)
    msa_descripcion = db.Column('msa_descripcion', db.Text)
    
    @staticmethod
    def get_by_id(id):
        return domo_mesa.query.filter_by(msa_id = id).first()
    
class domo_tipodepago(db.Model):
    __tablename__ = 'domo_tipodepago'
    tpg_id = db.Column('tpg_id', db.Integer, primary_key = True)
    tpg_etiqueta =  db.Column('tpg_etiqueta', db.String(30))
    tpg_descripcion = db.Column('tpg_descripcion', db.String(50))
    
class domo_restaurante(db.Model):
    __tablename__ = 'domo_restaurante'
    rtr_id = db.Column('rtr_id', db.Integer, primary_key = True)
    dir_id = db.Column('dir_id', db.Integer, db.ForeignKey('domo_direccion.dir_id'))
    tpr_id = db.Column('tpr_id', db.Integer)
    rtr_nombre = db.Column('rtr_nombre', db.String(50))
    rtr_rutacarta = db.Column('rtr_carta', db.Text)
    rtr_descripcion = db.Column('rtr_descripcion', db.Text)
    rtr_opvega = db.Column('rtr_opvega', db.Boolean)
    rtr_opvege = db.Column('rtr_opvege', db.Boolean)
    rtr_duenonombre = db.Column('rtr_nombredueno', db.String(40))
    rtr_duenoapellido = db.Column('rtr_apellidodueno', db.String(40))

    @staticmethod
    def get_by_id(id):
        return domo_restaurante.query.filter_by(rtr_id = id).first()
    
class domo_usuario(db.Model):
    __tablename__ = 'domo_usuario'
    usr_id = db.Column('usr_id', db.Integer, primary_key = True)
    tip_id = db.Column('tip_id', db.Integer, db.ForeignKey('domo_tipousuario.tip_id'))
    usr_login = db.Column('usr_login', db.String(20))
    usr_contrasena = db.Column('usr_contrasena', db.String(80))
    usr_estado = db.Column('usr_estado', db.String(20))
    
    @staticmethod
    def get_by_id(id):
        return domo_usuario.query.filter_by(usr_id = id).first()

class domo_encargadortr(db.Model):
    __tablename__ = 'domo_encargadortr'
    enc_id = db.Column('enc_id', db.Integer, primary_key = True)
    usr_id = db.Column('usr_id', db.Integer)
    rtr_id = db.Column('rtr_id', db.Integer)
    enc_nombre = db.Column('enc_nombre', db.String(40))
    enc_apellido = db.Column('enc_apellido', db.String(40))

class domo_cliente(db.Model):
    __tablename__ = 'domo_cliente'
    cli_id = db.Column('cli_id', db.Integer, primary_key = True)
    usr_id = db.Column('usr_id', db.Integer)
    cli_nombre = db.Column('cli_nombre', db.String(40))
    cli_apellido = db.Column('cli_apellido', db.String(40))
    dir_id = db.Column('dir_id', db.Integer)
    cli_telefono = db.Column('cli_telefono', db.String(20))
    cli_rut = db.Column('cli_rut', db.String(20))
    cli_tipo = db.Column('cli_tipo', db.String(1))
    
    @staticmethod
    def get_by_id(id):
        return domo_cliente.query.filter_by(cli_id = id).first()