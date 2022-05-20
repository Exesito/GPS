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

