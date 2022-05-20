from flask_sqlalchemy import SQLAlchemy
import json

from sqlalchemy import true

db = SQLAlchemy()

class domo_horario(db.Model):
    hor_id = db.Column(db.Integer, primary_key = true)
    rtr_id = db.Column(db.Integer)
    hor_diainicio = db.Column(db.Integer)
    hor_diatermino = db.Column(db.Integer)
    hor_horainicio = db.Column(db.Time)
    hor_horatermino = db.Column(db.Time)
    hor_disponibilidad = db.Column(db.Boolean)

class domo_rtr(db.Model):
    rtr_id = db.Column(db.Integer, primary_key = true)
    dir_id = db.Column(db.Integer)
    tpr_id = db.Column(db.Integer)
    rtr_nombre = db.Column(db.String(50))
    rtr_rutacarta = db.Column(db.Text)

