from flask_sqlalchemy import SQLAlchemy
import json
from flask_security import Security, SQLAlchemyUserDatastore, UserMixin
from sqlalchemy import func, desc
import bcrypt
from sqlalchemy import true
from datetime import date, datetime

db = SQLAlchemy()

class domo_reserva(db.Model):
    
    __tablename__ = 'domo_reserva'
    rsv_id = db.Column('rsv_id', db.Integer, primary_key = True)
    msa_id = db.Column('msa_id', db.Integer, db.ForeignKey('domo_mesa.msa_id'))
    tpg_id = db.Column('tpg_id', db.Integer, db.ForeignKey('domo_tipodepago.tpg_id'))
    cli_id = db.Column('cli_id', db.Integer, db.ForeignKey('domo_cliente.cli_id'))
    rsv_hora = db.Column('rsv_hora', db.Time)
    rsv_fecha = db.Column('rsv_fecha', db.Date)
    rsv_estado = db.Column('rsv_estado', db.String(30))
    rsv_fechaderegistro = db.Column('rsv_fechaderegistro', db.Date)
    #Columna de estatus Fail/Success
    
    def add_into_database(self):
        
        if(self.can_reserva): return False
        
        db.session.add(self)
        db.session.commit()
        
        return True
    
    def can_reserva(self):
        
        if not (self.verify_fecha): return False
        if not (self.verify_horario): return False
        
        return True
    
    def verify_fecha(self):
        
        if self.rsv_fechaderegistro > self.rsv_fecha: return False
        
        return True


    def verify_horario(self):

        if domo_horario.verify_horario_rtr(self.rsv_fecha, self.rsv_hora): return True

        return False

    #Retorna todas las reservas del restaurante asociado
    def get_by_id_restaurante(id):

        query = domo_restaurante.query.join(domo_mesa).join(domo_reserva).filter(domo_restaurante.rtr_id == id).all()
        return query
    
    def get_restaurante(self):

        query = db.session.query(domo_reserva, domo_mesa, domo_restaurante).filter(domo_reserva.msa_id == domo_mesa.msa_id, domo_mesa.rtr_id == domo_restaurante.rtr_id, domo_reserva.rsv_id == self.rsv_id).first()
        print(query)
        return query.domo_restaurante.rtr_id
    
    def error(self):
        
        self.rsv_estado = "FALLIDA"
        db.session.commit()
        
        return
    
    @staticmethod
    def get_by_id(id):
        return domo_reserva.query.filter_by(rsv_id = id).first()
    
    def get_cliente(self):
        return domo_cliente.query.filter(domo_cliente.cli_id == self.cli_id).first()

    @staticmethod
    def get_by_id(id):
        return domo_reserva.query.filter_by(rsv_id = id).first()
    
    
    @staticmethod
    def get_reservas_today():
        return domo_reserva.query.filter_by(domo_reserva.rsv_fecha == date.today(), 
                                            domo_reserva.rsv_hora >= datetime.time(8,0,0), 
                                            domo_reserva.rsv_estado == "REALIZADA")

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

    def get_by_restaurante(id):
        aforo = domo_aforo.query.filter(domo_aforo.rtr_id == id).first()
        if aforo != None:
            return aforo    
        

class domo_tiporestaurante(db.Model):
    __tablename__ = 'domo_tiporestaurante'
    tpr_id = db.Column('tpr_id', db.Integer, primary_key = true)
    tpr_nombre = db.Column('tpr_nombre', db.String(40))
    tpr_descripcion = db.Column('tpr_descripcion', db.Text)

class domo_mesa(db.Model):
    __tablename__ = 'domo_mesa'
    rtr_id = db.Column('rtr_id', db.Integer, db.ForeignKey('domo_restaurante.rtr_id'))
    msa_id = db.Column('msa_id', db.Integer, primary_key = True)
    msa_numero = db.Column('msa_numero', db.Integer)
    msa_capacidad = db.Column('msa_capacidad', db.Integer)
    msa_descripcion = db.Column('msa_descripcion', db.Text)
    
    @staticmethod
    def get_by_id(id):
        return domo_mesa.query.filter_by(msa_id = id).first() 

class domo_restaurante(db.Model):
    __tablename__ = 'domo_restaurante'
    rtr_id = db.Column('rtr_id', db.Integer, primary_key = True)
    dir_id = db.Column('dir_id', db.Integer, db.ForeignKey('domo_direccion.dir_id'))
    tpr_id = db.Column('tpr_id', db.Integer)
    rtr_nombre = db.Column('rtr_nombre', db.String(50))
    rtr_descripcion = db.Column('rtr_descripcion', db.Text)
    rtr_opvega = db.Column('rtr_opvega', db.Boolean)
    rtr_opvege = db.Column('rtr_opvege', db.Boolean)
    rtr_duenonombre = db.Column('rtr_duenonombre', db.String(40))
    rtr_duenoapellido = db.Column('rtr_duenoapellido', db.String(40))
    rtr_cantidadmesas = db.Column('rtr_cantidadmesas', db.Integer)
    rtr_cantidadsillas = db.Column('rtr_cantidadsillas', db.Integer)
    rtr_visible = db.Column('rtr_visible', db.Boolean)
    
    def get_mesas(self):
        return domo_mesa.query.filter_by(rtr_id = self.rtr_id).all()
    
    def generate_reserva(self, hora, fecha, mesa_id, estado):    
        
        hora = "%d:00:00" % (int(hora))
        max_id_rsv = db.session.query(func.max(domo_reserva.rsv_id)).scalar() + 1
        new_reserva = domo_reserva(rsv_id = max_id_rsv, rsv_hora = hora, rsv_fecha = fecha, rsv_estado = estado, msa_id = mesa_id, rsv_fechaderegistro = date.today())     
        db.session.add(new_reserva)
        db.session.commit()
        
        return new_reserva.rsv_id
        
    def calcular_mesas(self):
        mesas = 0
        sillas = 0
        mesaQuery = self.get_mesas()
        
        for n in mesaQuery:
            mesas  += 1
            sillas += n.msa_capacidad
        
        self.rtr_cantidadmesas = mesas
        self.rtr_cantidadsillas = sillas
        
        aforo = self.get_aforo()
        aforo.afo_capacidadmax = sillas
        db.session.commit()

    def get_aforo(self):
        afo = domo_aforo.query.filter(domo_aforo.rtr_id == self.rtr_id).first()
        if  afo == None:
            max_aforo_id = db.session.query(func.max(domo_aforo.afo_id)).scalar() + 1
            afo = domo_aforo(afo_id = max_aforo_id, rtr_id = self.rtr_id, afo_capacidadactual = 0, afo_capacidadmax = self.rtr_cantidadsillas)
            db.session.add(afo)
            db.session.commit()
        return afo

    @staticmethod
    def get_reservas(id):
        
        query = db.session.query(domo_restaurante, domo_cliente, domo_mesa, domo_reserva).filter(
            domo_restaurante.rtr_id == domo_mesa.rtr_id,
            domo_mesa.msa_id == domo_reserva.msa_id,
            domo_reserva.cli_id == domo_cliente.cli_id,
            domo_restaurante.rtr_id == id,
            domo_reserva.rsv_estado != "PROCESANDO"
        ).all()
        
        return query
    
    @staticmethod
    def get_valoraciones(id):
        
        query = db.session.query(domo_valoracion).filter(
            domo_restaurante.rtr_id == domo_mesa.rtr_id,
            domo_mesa.msa_id == domo_reserva.msa_id,
            domo_valoracion.rsv_id == domo_reserva.rsv_id,
            domo_restaurante.rtr_id == id
        ).order_by(desc(domo_valoracion.val_id)).all()
        
        return query
    @staticmethod
    def get_valoraciones_max(id, max):
        
        query = db.session.query(domo_valoracion).filter(
            domo_restaurante.rtr_id == domo_mesa.rtr_id,
            domo_mesa.msa_id == domo_reserva.msa_id,
            domo_valoracion.rsv_id == domo_reserva.rsv_id,
            domo_restaurante.rtr_id == id
        ).order_by(desc(domo_valoracion.val_id)).limit(max).all()
        
        return query
    
    @staticmethod
    def get_by_id(id):
        return domo_restaurante.query.filter_by(rtr_id = id).first()
    
class domo_tipodepago(db.Model):
    __tablename__ = 'domo_tipodepago'
    tpg_id = db.Column('tpg_id', db.Integer, primary_key = true)
    tpg_etiqueta =  db.Column('tpg_etiqueta', db.String(30))
    tpg_descripcion = db.Column('tpg_descripcion', db.String(50))

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
    
    @staticmethod
    def get_by_id(id):
        return domo_usuario.query.filter_by(usr_id = id).first()
    
    @staticmethod
    def get_by_cliente(id):
        cliente = domo_cliente.query.filter(domo_cliente.cli_id == id).first()
        return domo_usuario.query.filter(cliente.usr_id == domo_usuario.usr_id).first()
        
class domo_encargadortr(db.Model):
    __tablename__ = 'domo_encargadortr'
    enc_id = db.Column('enc_id', db.Integer, primary_key = true)
    usr_id = db.Column('usr_id', db.Integer)
    rtr_id = db.Column('rtr_id', db.Integer)
    enc_rut = db.Column('enc_rut', db.String(13))
    enc_nombre = db.Column('enc_nombre', db.String(40))
    enc_apellido = db.Column('enc_apellido', db.String(40))

class domo_cliente(db.Model):
    __tablename__ = 'domo_cliente'
    cli_id = db.Column('cli_id', db.Integer, primary_key = True, autoincrement=True)
    usr_id = db.Column('usr_id', db.Integer)
    cli_nombre = db.Column('cli_nombre', db.String(40))
    cli_apellido = db.Column('cli_apellido', db.String(40))
    dir_id = db.Column('dir_id', db.Integer)
    cli_telefono = db.Column('cli_telefono', db.String(20))
    cli_correo = db.Column('cli_correo', db.String(40))
    cli_rut = db.Column('cli_rut', db.String(20))
    
    @staticmethod 
    def get_by_usr_id(usr_id):
        query = domo_cliente.query.filter(domo_cliente.usr_id == usr_id).first()
        return query
    
    @staticmethod 
    def get_reservas(id):
        
        query = db.session.query(domo_reserva, domo_mesa, domo_restaurante, domo_valoracion).join(
            domo_valoracion, domo_valoracion.rsv_id == domo_reserva.rsv_id, isouter=True
            ).filter(
            domo_reserva.cli_id == id,
            domo_reserva.msa_id == domo_mesa.msa_id,
            domo_restaurante.rtr_id == domo_mesa.rtr_id,
            domo_reserva.rsv_estado != "PROCESANDO"
        ).all()
        return query

    @staticmethod
    def get_by_rut(rut): #rut sin puntos ni guion
        return domo_cliente.query.filter_by(cli_rut = rut).first()
    
    @staticmethod
    def get_by_id(id):
        return domo_cliente.query.filter_by(cli_id = id).first()
    
    @staticmethod
    def get_by_cliente(id):
        cliente = domo_cliente.query.filter_by(domo_cliente.cli_id == id).first()
        return domo_usuario.query.filter_by(cliente.usr_id == domo_usuario.usr_id).first()
    
class domo_horario(db.Model):
    __tablename__ = 'domo_horario'
    hor_id = db.Column('hor_id', db.Integer, primary_key = True)
    rtr_id = db.Column('rtr_id', db.Integer ,db.ForeignKey('domo_restaurante.rtr_id'))
    hor_nombre = db.Column('hor_nombre', db.String(20))
    hor_diainicio = db.Column('hor_diainicio', db.Integer)
    hor_diatermino = db.Column('hor_diatermino', db.Integer)
    hor_horainicio = db.Column('hor_horainicio', db.Time)
    hor_horatermino = db.Column('hor_horatermino', db.Time)
    hor_activo = db.Column('hor_activo', db.Boolean)

    def verify_horario_rtr(self, day, hour):
        
        if (self.hor_diainicio < hour < self.hor_diatermino):
            return True

        return False

    @staticmethod
    def get_by_id_rest(id):
        return domo_horario.query.filter_by(rtr_id = id).all()

class domo_carta(db.Model):
    __tablename__ = 'domo_carta'
    car_id = db.Column('car_id', db.Integer, primary_key = true)
    rtr_id = db.Column('rtr_id', db.Integer)
    car_nombre = db.Column('car_nombre', db.String(20))
    car_url = db.Column('car_url', db.String(255))
    car_activa = db.Column('car_activa', db.Boolean)

class domo_valoracion(db.Model):
    __tablename__ = 'domo_valoracion'
    val_id = db.Column('val_id', db.Integer, primary_key = True)
    rsv_id = db.Column('rsv_id', db.Integer ,db.ForeignKey('domo_reserva.rsv_id'))
    val_descripcion = db.Column('val_descripcion', db.String(255))
    val_estrella = db.Column('val_estrella', db.Integer)
    
    @staticmethod
    def valorar(rsv_id, text, valor):
        
        query = domo_valoracion.query.filter(domo_valoracion.rsv_id == rsv_id).first()
        
        if query is None:
            
            max_id = db.session.query(func.max(domo_valoracion.val_id)).scalar() + 1
            new_valoracion = domo_valoracion(val_id = max_id, rsv_id = rsv_id, val_descripcion = text, val_estrella = valor)
            db.session.add(new_valoracion)
        
        else:
            
            query.val_descripcion = text
            query.val_estrella = valor
            
        db.session.commit()
        
        return
    
    @staticmethod
    def delete(rsv_id):
        
        query = domo_valoracion.query.filter(domo_valoracion.rsv_id == rsv_id).first()
        db.session.delete(query)
        db.session.commit()
        
        return

class domo_correo_produccion(db.Model):
    __tablename__ = 'domo_correos_produccion'
    correo_id = db.Column('correo_id', db.Integer, primary_key = True)
    correo = db.Column('correo', db.String(50))
    contraseña = db.Column('contraseña', db.String(50))

    @staticmethod
    def get_main():
        return domo_correo_produccion.query.first()