from wtforms import Form, SubmitField, StringField, PasswordField, validators, SelectField, DateField, RadioField, IntegerField, EmailField
from datetime import date
from wtforms.validators import InputRequired, Email

class ReservaForm(Form):
    
    dia = DateField('Día', default= date.today())
    hora = SelectField('Hora', choices=[])
    submit = SubmitField("Reservar")
    
class ClientForm(Form):

    nombre = StringField('Nombre', [validators.DataRequired(), validators.Length(min=1, max=12)])
    apellido = StringField('Apellido', [validators.Length(min=1, max=12)])
    telefono = StringField('Telefono', [validators.DataRequired(), validators.Length(min=1, max=12)])
    rut = StringField('Rut', [validators.DataRequired(), validators.Length(min=1, max=12)])
    direccion = StringField('Dirección', [validators.Length(min=1, max=60)])
    email = StringField('Correo Eléctronico', [InputRequired("Ingrese un Email"), Email("Ingrese un email valido."), validators.Length(min=6, max=35)])
    medio_de_pago = RadioField("Medio de Pago", [validators.DataRequired()] , choices=[("DEBITO",'Débito (Presencial)'), ("EFECTIVO","Efectivo"), ("WEBPAY","")])
    
    submit = SubmitField("Completar Reserva y pagar")
    
class MesaForm(Form):
    
    mesa = SelectField("Mesa", choices=[])
    submit = SubmitField("Seleccionar Mesa")

class RegisterForm(Form):
    values=[0]
    #username = StringField('', [validators.Length(min=4, max=25)])
    email = StringField('Correo Eléctronico', [validators.DataRequired(message='Ingrese email'), validators.Email(), validators.Length(min=6, max=50)])
    password = PasswordField('Nueva Contraseña', [validators.DataRequired(message='Ingrese contraseña'),validators.Length(min=3,max=16)])
    confirm = PasswordField('Repite Contraseña', [validators.DataRequired(message='Ingrese contraseña nuevamente'),validators.EqualTo('password', message='Las contraseñas deben coincidir'),validators.Length(min=3,max=16)])
    nombre= StringField('Nombre', [validators.DataRequired(message='Ingrese nombre'),  validators.Length(min=3, max=35)])
    apellido= StringField('Apellido', [validators.DataRequired(message='Ingrese apellido'), validators.Length(min=2, max=35)])
    rut= StringField('Rut', [validators.DataRequired(message='Ingrese rut'), validators.Length(min=6, max=13)])
    celular=IntegerField('Celular',[validators.Length(min=5,max=15)])#,[validators.DataRequired()]
    region=SelectField('Región',[validators.AnyOf(values,message='Seleccione una región',values_formatter=None)])
    ciudad=SelectField('Ciudad',[validators.AnyOf(values,message='Seleccione una ciudad',values_formatter=None)])
    calle=StringField('Calle', [validators.DataRequired(message='Ingrese nombre de la calle')])
    numero=IntegerField('Número', [validators.DataRequired(message='Ingrese numero de la dirección')])
    #tipo=SelectField('Tipo')

    submit = SubmitField("Crear Cuenta")

class LoginForm(Form):
    email=EmailField('Correo electrónico',[validators.DataRequired(message='Ingrese email'), validators.Email(), validators.Length(min=6, max=50)])
    password= PasswordField('Contraseña', [validators.DataRequired(message='Ingrese contraseña')])

    submit=SubmitField('Iniciar sesión')

class RecoveryForm(Form):
    email=EmailField('Correo electrónico',[validators.DataRequired(),validators.Email(),validators.Length(min=6,max=35)])
    submit=SubmitField('Recuperar acceso')

class ChangepasswordForm(Form):
    password= PasswordField('Nueva contraseña',[validators.DataRequired(),validators.EqualTo('confirm', message='Las contraseñas deben coincidir')])
    confirm= PasswordField('Repite contraseña', [validators.DataRequired()])
    submit= SubmitField("Cambiar contraseña")

class RegistroEncargado(Form):
    values=[0]
    email = StringField('Correo Eléctronico', [validators.DataRequired(message='Ingrese email'), validators.Email(), validators.Length(min=6, max=50)])
    password = PasswordField('Nueva Contraseña', [validators.DataRequired(message='Ingrese contraseña'),validators.EqualTo('confirm', message='Las contraseñas deben coincidir'),validators.Length(min=3,max=16)])
    confirm = PasswordField('Repite contraseña', [validators.DataRequired(message='Ingrese contraseña nuevamente'), validators.Length(min=6, max=16)])
    nombre= StringField('Nombre', [validators.DataRequired(message='Ingrese nombre del encargado'),  validators.Length(min=3, max=35)])
    apellido= StringField('Apellido', [validators.DataRequired(message='Ingrese apellido del encargado'), validators.Length(min=2, max=35)])
    rut= StringField('Rut', [validators.DataRequired(message='Ingrese rut del encargado'), validators.Length(min=6, max=13)])
    estado= SelectField('Estado de la cuenta', choices=[('ACTIVA','Activa'),('INACTIVA','Inactiva'),('BANEADA','Baneada'),('PENDIENTE','Pendiente')])
    restaurante=SelectField('Restaurante',[validators.AnyOf(values,message='Seleccione un restaurante',values_formatter=None)])
    submit = SubmitField('Crear Cuenta')

class RegistroAdmin(Form):
    email = StringField('Correo Eléctronico', [validators.DataRequired(message='Ingrese email'), validators.Email(), validators.Length(min=6, max=50)])
    password = PasswordField('Nueva Contraseña', [validators.DataRequired(message='Ingrese contraseña'),validators.EqualTo('confirm', message='Las contraseñas deben coincidir'),validators.Length(min=3,max=16)])
    confirm = PasswordField('Repite contraseña', [validators.DataRequired(message='Ingrese contraseña nuevamente'), validators.Length(min=6, max=16)])
    estado= SelectField('Estado de la cuenta', choices=[('ACTIVA','Activa'),('INACTIVA','Inactiva'),('BANEADA','Baneada'),('PENDIENTE','Pendiente')])

    submit = SubmitField('Crear Cuenta')


class EditForm3(Form):
    email = StringField('Correo Eléctronico', [validators.DataRequired(message='Ingrese email'), validators.Email(), validators.Length(min=6, max=35)])
    password = PasswordField('Nueva Contraseña', [validators.Length(min=0, max=16)])
    estado= SelectField('Estado de la cuenta', choices=[('ACTIVA','ACTIVA'),('INACTIVA','INACTIVA'),('BANEADA','BANEADA'),('PENDIENTE','PENDIENTE')])
    submit= SubmitField("Guardar Cambios")

class EditForm2(Form):
    values=[0]
    email = StringField('Correo Eléctronico', [validators.DataRequired(message='Ingrese email'), validators.Email(), validators.Length(min=6, max=35)])
    password = PasswordField('Nueva Contraseña', [validators.Length(min=0, max=16)])
    nombre= StringField('Nombre', [validators.DataRequired(),  validators.Length(min=3, max=35)])
    apellido= StringField('Apellido', [validators.DataRequired(), validators.Length(min=2, max=35)])
    rut= StringField('Rut', [validators.DataRequired(), validators.Length(min=6, max=13)])
    estado= SelectField('Estado de la cuenta', choices=[('ACTIVA','ACTIVA'),('INACTIVA','INACTIVA'),('BANEADA','BANEADA'),('PENDIENTE','PENDIENTE')])
    restaurante=SelectField('Restaurante',[validators.AnyOf(values,message='Seleccione un restaurante',values_formatter=None)])

    submit= SubmitField('Guardar Cambios')

class EditForm1(Form):
    values=[0]
    email = StringField('Correo Eléctronico', [validators.DataRequired(message='Ingrese email'), validators.Email(), validators.Length(min=6, max=35)])
    password = PasswordField('Nueva Contraseña', [validators.Length(min=0, max=16)])
    estado= SelectField('Estado de la cuenta', choices=[('ACTIVA','ACTIVA'),('INACTIVA','INACTIVA'),('BANEADA','BANEADA'),('PENDIENTE','PENDIENTE')])
    nombre= StringField('Nombre', [validators.DataRequired(),  validators.Length(min=3, max=35)])
    apellido= StringField('Apellido', [validators.DataRequired(), validators.Length(min=2, max=35)])
    rut= StringField('Rut', [validators.DataRequired(), validators.Length(min=6, max=13)])
    celular=IntegerField('Celular',[validators.Length(min=5,max=15)])#,[validators.DataRequired()]
    region=SelectField('Región',[validators.AnyOf(values,message='Seleccione una región',values_formatter=None)])
    ciudad=SelectField('Ciudad',[validators.AnyOf(values,message='Seleccione una ciudad',values_formatter=None)])
    calle=StringField('Calle', [validators.DataRequired()])
    numero=IntegerField('Número', [validators.DataRequired()])


    submit= SubmitField('Guardar Cambios')



class IngresarRestaurante(Form):  

    values = [0]  
    nombre=StringField('Nombre',[validators.Length(min=6, max=35),validators.DataRequired()])
    calle=StringField('Calle',[validators.Length(min=6, max=35),validators.DataRequired()])
    numero=IntegerField('Numero',[validators.Length(min=6, max=35),validators.DataRequired()])
    ciudad=SelectField('Ciudad',[validators.AnyOf(values,message='Seleccione una ciudad',values_formatter=None)])
    region=SelectField('Region',[validators.AnyOf(values,message='Seleccione una región',values_formatter=None)])
    dueno=StringField('Nombre del dueño',[validators.Length(min=6, max=35),validators.DataRequired()])
    apellido_dueno=StringField('Apellido del dueño',[validators.Length(min=6, max=35),validators.DataRequired()])
    descripcion=StringField('Descripcion',[validators.Length(min=6, max=35),validators.DataRequired()])
    tipo_restaurante=SelectField('Tipo de restaurante',[validators.Length(min=6, max=35),validators.DataRequired()])
    vegetariana=SelectField('Vegetariana',choices=[('Si','Si'),('No','No')])
    vegana=SelectField('Vegana',choices=[('Si','Si'),('No','No')])

    #direccion=StringField('Dirección',[validators.Length(min=6, max=35)])
    submit=SubmitField('Ingresar')


