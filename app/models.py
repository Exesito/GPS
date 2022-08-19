from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore, UserMixin
import bcrypt

db = SQLAlchemy()

from flask_sqlalchemy import SQLAlchemy
import json

from sqlalchemy import true

db = SQLAlchemy()

class domo_horario(db.Model):
    __tablename__ = 'domo_horario'
    hor_id = db.Column('hor_id', db.Integer, primary_key = true)
    rtr_id = db.Column('rtr_id', db.Integer ,db.ForeignKey('domo_rtr.rtr_id'))
    hor_diainicio = db.Column('hor_diainicio', db.Integer)
    hor_diatermino = db.Column('hor_diatermino', db.Integer)
    hor_horainicio = db.Column('hor_horainicio', db.Time)
    hor_horatermino = db.Column('hor_horatermino', db.Time)
    hor_disponibilidad = db.Column('hor_disponibilidad', db.Boolean)

class domo_restaurante(db.Model):
    __tablename__ = 'domo_restaurante'
    rtr_id = db.Column('rtr_id', db.Integer, primary_key = true)
    dir_id = db.Column('dir_id', db.Integer, db.ForeignKey('domo_direccion.dir_id'))
    tpr_id = db.Column('tpr_id', db.Integer)
    rtr_nombre = db.Column('rtr_nombre', db.String(50))
    rtr_rutacarta = db.Column('rtr_carta', db.Text)
    rtr_descripcion = db.Column('rtr_descripcion', db.Text)
    rtr_opvega = db.Column('rtr_opvega', db.Boolean)
    rtr_opvege = db.Column('rtr_opvege', db.Boolean)
    rtr_duenonombre = db.Column('rtr_nombredueno', db.String(40))
    rtr_duenoapellido = db.Column('rtr_apellidodueno', db.String(40))

class domo_direccion(db.Model):
    __tablename__ = 'domo_direccion'
    dir_id = db.Column('dir_id', db.Integer, primary_key = true)
    ciu_id = db.Column('ciu_id', db.Integer, db.ForeignKey('domo_ciudad.ciu_id'))
    dir_nombrecalle = db.Column('dir_nombrecalle', db.String(50))
    dir_numerocalle = db.Column('dir_numerocalle', db.Integer)

class domo_ciudad(db.Model):
    __tablename__ = 'domo_ciudad'
    ciu_id = db.Column('ciu_id', db.Integer, primary_key = true)
    reg_id = db.Column('reg_id', db.Integer, db.ForeignKey('domo_region.reg_id'))
    ciu_nombre = db.Column('ciu_nombre', db.String(40))

class domo_region(db.Model):
    __tablename__ = 'domo_region'
    reg_id = db.Column('reg_id', db.Integer, primary_key = true)
    reg_nombre = db.Column('reg_nombre', db.String(30))

class domo_aforo(db.Model):
    afo_id = db.Column('afo_id', db.Integer, primary_key = true)
    rtr_id = db.Column('rtr_id', db.Integer, db.ForeignKey('domo_region.reg_id'))
    afo_capacidadmax = db.Column('afo_capacidadmax', db.Integer)
    afo_capacidadactual = db.Column('afo_capacidadactual', db.Integer)

class domo_tiporestaurante(db.Model):
    __tablename__ = 'domo_tiporestaurante'
    tpr_id = db.Column('tpr_id', db.Integer, primary_key = true)
    tpr_nombre = db.Column('tpr_nombre', db.String(40))
    tpr_descripcion = db.Column('tpr_descripcion', db.Text)

class domo_mesa(db.Model):
    __tablename__ = 'domo_mesa'
    rtr_id = db.Column('rtr_id', db.Integer, db.ForeignKey('domo_rtr.rtr_id'))
    msa_id = db.Column('msa_id', db.Integer, primary_key = true)
    msa_numero = db.Column('msa_numero', db.Integer)
    msa_capacidad = db.Column('msa_capacidad', db.Integer)
    msa_descripcion = db.Column('msa_descripcion', db.Text)

class domo_tipodepago(db.Model):
    __tablename__ = 'domo_tipodepago'
    tpg_id = db.Column('tpg_id', db.Integer, primary_key = true)
    tpg_etiqueta =  db.Column('tpg_etiqueta', db.String(30))
    tpg_descripcion = db.Column('tpg_descripcion', db.String(50))

class domo_reserva(db.Model):
    __tablename__ = 'domo_reserva'
    rsv_id = db.Column('rsv_id', db.Integer, primary_key = true)
    msa_id = db.Column('msa_id', db.Integer, db.ForeignKey('domo_mesa.msa_id'))
    tpg_id = db.Column('tpg_id', db.Integer, db.ForeignKey('domo_tipodepago.tpg_id'))
    rsv_hora = db.Column('rsv_hora', db.Time)
    rsv_fecha = db.Column('rsv_fecha', db.Date)
    rsv_asistencia = db.Column('rsv_asistencia', db.String(30))
    rsv_fechaderegistro = db.Column('rsv_fechaderegistro', db.Date)

class domo_tipousuario(db.Model):
    __tablename__ = 'domo_tipousuario'
    tip_id = db.Column('tip_id', db.Integer, primary_key = true)
    tip_nombre = db.Column('tip_nombre', db.String(20))
    tip_descripcion = db.Column('tip_descripcion', db.Text)

class domo_usuario(db.Model, UserMixin):
    __tablename__ = 'domo_usuario'
    usr_id = db.Column('usr_id', db.Integer, primary_key = true)
    tip_id = db.Column('tip_id', db.Integer, db.ForeignKey('domo_tipousuario.tip_id'))
    usr_login = db.Column('usr_login', db.String(40))
    usr_contrasena = db.Column('usr_contrasena', db.String(80))
    usr_estado = db.Column('usr_estado', db.String(20))

    @property
    def password(self):
        raise AttributeError('password not readable')
    @password.setter
    def password(self, password):

        pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        self.usr_contrasena=pw.decode('utf-8')
        print(self.usr_contrasena)
        
    def verify_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.usr_contrasena)
    
    def __init__(self, id, tipo,email,password,estado):
        self.usr_id=id
        self.tip_id = tipo #Tipo de Usuario Cliente
        self.usr_login = email
        self.password = password
        self.usr_estado = estado


class domo_encargadortr(db.Model):
    __tablename__ = 'domo_encargadortr'
    enc_id = db.Column('enc_id', db.Integer, primary_key = true)
    usr_id = db.Column('usr_id', db.Integer)
    rtr_id = db.Column('rtr_id', db.Integer)
    enc_nombre = db.Column('enc_nombre', db.String(40))
    enc_apellido = db.Column('enc_apellido', db.String(40))

class domo_cliente(db.Model):
    __tablename__ = 'domo_cliente'
    cli_id = db.Column('cli_id', db.Integer, primary_key = true)
    usr_id = db.Column('usr_id', db.Integer)
    cli_nombre = db.Column('cli_nombre', db.String(40))
    cli_apellido = db.Column('cli_apellido', db.String(40))
    dir_id = db.Column('dir_id', db.Integer)
    cli_telefono = db.Column('cli_telefono', db.Integer)
    cli_rut = db.Column('cli_rut', db.String(13))
    cli_tipo = db.Column('cli_tipo', db.String(1))