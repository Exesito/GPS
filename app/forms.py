from wtforms import Form, SubmitField, StringField, PasswordField, validators, SelectField, DateField, RadioField
from datetime import date
  
class RegisterForm(Form):
    
    #username = StringField('', [validators.Length(min=4, max=25)])
    email = StringField('Correo Eléctronico', [validators.Length(min=6, max=35)])
    password = PasswordField('Nueva Contraseña', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Las contraseñas deben coincidir')
    ])
    confirm = PasswordField('Repite contraseña')
    submit = SubmitField("Crear Cuenta")

class ReservaForm(Form):
    
    dia = DateField('Día', default= date.today())
    hora = SelectField('Hora', choices=[])
    submit = SubmitField("Reservar")
    
class ClientForm(Form):

    nombre = StringField('Nombre', [validators.Length(min=1, max=12)])
    apellido = StringField('Apellido', [validators.Length(min=1, max=12)])
    telefono = StringField('Telefono', [validators.Length(min=1, max=12)])
    rut = StringField('Rut', [validators.Length(min=1, max=12)])
    direccion = StringField('Dirección', [validators.Length(min=1, max=60)])
    medio_de_pago = RadioField("Medio de Pago", choices=[("DEBITO",'Débito (Presencial)'), ("EFECTIVO","Efectivo"), ("WEBPAY","")])
    
    submit = SubmitField("Completar Reserva y pagar")
    
class MesaForm(Form):
    
    mesa = SelectField("Mesa", choices=[])
    submit = SubmitField("Seleccionar Mesa")