from flask_sqlalchemy import SQLAlchemy
import json

from sqlalchemy import true

db = SQLAlchemy()

class domo_horario(db.Model):
    hor_id = db.Column(db.Integer, primary_key = true)
    rtr_id = db.Column(db.Integer ,db.ForeignKey('domo_rtr.rtr_id'))
    hor_diainicio = db.Column(db.Integer)
    hor_diatermino = db.Column(db.Integer)
    hor_horainicio = db.Column(db.Time)
    hor_horatermino = db.Column(db.Time)
    hor_disponibilidad = db.Column(db.Boolean)

class domo_rtr(db.Model):
    rtr_id = db.Column(db.Integer, primary_key = true)
    dir_id = db.Column(db.Integer, db.ForeignKey('domo_direccion.dir_id'))
    tpr_id = db.Column(db.Integer)
    rtr_nombre = db.Column(db.String(50))
    rtr_rutacarta = db.Column(db.Text)
    rtr_descripcion = db.Column(db.Text)
    rtr_opvega = db.Column(db.Boolean)
    rtr_opvege = db.Column(db.Boolean)
    rtr_duenonombre = db.Column(db.String(40))
    rtr_duenoapellido = db.Column(db.String(40))

class domo_direccion(db.Model):
    dir_id = db.Column(db.Integer, primary_key = true)
    ciu_id = db.Column(db.Integer, db.ForeignKey('domo_ciudad.ciu_id'))
    dir_nombrecalle = db.Column(db.String(50))
    dir_numerocalle = db.Column(db.Integer)

class domo_ciudad(db.Model):
    ciu_id = db.Column(db.Integer, primary_key = true)
    reg_id = db.Column(db.Integer, db.ForeignKey('domo_region.reg_id'))
    ciu_nombre = db.Column(db.String(40))

class domo_region(db.Model):
    reg_id = db.Column(db.Integer, primary_key = true)
    reg_nombre = db.Column(db.String(30))

class domo_aforo(db.Model):
    afo_id = db.Column(db.Integer, primary_key = true)
    rtr_id = db.Column(db.Integer, db.ForeignKey('domo_region.reg_id'))
    afo_capacidadmax = db.Column(db.Integer)
    afo_capacidadactual = db.Column(db.Integer)

class domo_tiporestaurante(db.Model):
    tpr_id = db.Column(db.Integer, primary_key = true)
    tpr_nombre = db.Column(db.String(40))
    tpr_descripcion = db.Column(db.Text)

class domo_encargadortr(db.Model):
    enc_id = db.Column(db.Serial, primary_key = true)

class domo_mesa(db.Model):
    rtr_id = db.Column(db.Integer, db.ForeignKey('domo_rtr.rtr_id'))
    msa_id = db.Column(db.Integer, primary_key = true)
    msa_numero = db.Column(db.Integer)
    msa_capacidad = db.Column(db.Integer)
    msa_descripcion = db.Column(db.Text)

class domo_tipodepago(db.Model):
    tpg_id = db.Column(db.Serial, primary_key = true)
    tpg_etiqueta =  db.Column(db.String(30))
    tpg_descripcion = db.Column(db.String(50))

class domo_reserva(db.Model):
    rsv_id = db.Column(db.Serial, primary_key = true)
    msa_id = db.Column(db.Integer, db.ForeignKey('domo_mesa.msa_id'))
    tpg_id = db.Column(db.Integer, db.ForeignKey('domo_tipodepago.tpg_id'))
    rsv_hora = db.Column(db.Time)
    rsv_fecha = db.Column(db.Date)
    rsv_asistencia = db.Column(db.String(30))
    rsv_fechaderegistro = db.Column(db.Date)

class domo_tipousuario(db.Model):
    tip_id = db.Column(db.Serial, primary_key = true)
    tip_nombre = db.Column(db.String(20))
    tip_descripcion = db.Column(db.Text)

class domo_usuario(db.Model):
    usr_id = db.Column(db.Serial, primary_key = true)
    tip_id = db.Column(db.Integer, db.ForeignKey('domo_tipousuario.tip_id')
    usr_login = db.Column(db.String(20))
    usr_contrasena = db.Column(db.String(80))
    usr_estado = db.Column(db.String(20))
