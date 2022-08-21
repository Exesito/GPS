
from wtforms import Form, SubmitField, StringField, PasswordField, IntegerField, SelectField,validators
from wtforms import EmailField  

class RegisterForm(Form):
    values=[0]
    #username = StringField('', [validators.Length(min=4, max=25)])
    email = StringField('Correo Eléctronico', [validators.DataRequired(message='Ingrese email'), validators.Email(), validators.Length(min=6, max=35)])
    password = PasswordField('Nueva Contraseña', [validators.DataRequired(),validators.EqualTo('confirm', message='Las contraseñas deben coincidir')])
    confirm = PasswordField('Repite Contraseña', [validators.DataRequired()])
    nombre= StringField('Nombre', [validators.DataRequired(),  validators.Length(min=3, max=35)])
    apellido= StringField('Apellido', [validators.DataRequired(), validators.Length(min=2, max=35)])
    rut= StringField('Rut', [validators.DataRequired(), validators.Length(min=6, max=13)])
    celular=IntegerField('Celular',[validators.Length(min=5,max=15)])#,[validators.DataRequired()]
    region=SelectField('Región',[validators.AnyOf(values,message='Seleccione una región',values_formatter=None)])
    ciudad=SelectField('Ciudad',[validators.AnyOf(values,message='Seleccione una ciudad',values_formatter=None)])
    calle=StringField('Calle', [validators.DataRequired()])
    numero=IntegerField('Número', [validators.DataRequired()])
    #tipo=SelectField('Tipo')

    submit = SubmitField("Crear Cuenta")

class LoginForm(Form):
    email=EmailField('Correo electrónico',[validators.DataRequired(), validators.Email(), validators.Length(min=6, max=35)])
    password= PasswordField('Contraseña', [validators.DataRequired()])

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
    email = StringField('Correo Eléctronico', [validators.DataRequired(message='Ingrese email'), validators.Email(), validators.Length(min=6, max=35)])
    password = PasswordField('Nueva Contraseña', [validators.DataRequired(),validators.EqualTo('confirm', message='Las contraseñas deben coincidir')])
    confirm = PasswordField('Repite contraseña', [validators.DataRequired(), validators.Length(min=6, max=35)])
    nombre= StringField('Nombre', [validators.DataRequired(),  validators.Length(min=3, max=35)])
    apellido= StringField('Apellido', [validators.DataRequired(), validators.Length(min=2, max=35)])
    rut= StringField('Rut', [validators.DataRequired(), validators.Length(min=6, max=13)])
    estado= SelectField('Estado de la cuenta', choices=[('ACTIVA','Activa'),('INACTIVA','Inactiva'),('BANEADA','Baneada'),('PENDIENTE','Pendiente')])
    restaurante=SelectField('Restaurante',[validators.AnyOf(values,message='Seleccione un restaurante',values_formatter=None)])
    submit = SubmitField('Crear Cuenta')

class RegistroAdmin(Form):
    email = StringField('Correo Eléctronico', [validators.DataRequired(message='Ingrese email'), validators.Email(), validators.Length(min=6, max=35)])
    password = PasswordField('Nueva Contraseña', [validators.DataRequired(),validators.EqualTo('confirm', message='Las contraseñas deben coincidir')])
    confirm = PasswordField('Repite contraseña', [validators.DataRequired(), validators.Length(min=6, max=35)])
    estado= SelectField('Estado de la cuenta', choices=[('ACTIVA','Activa'),('INACTIVA','Inactiva'),('BANEADA','Baneada'),('PENDIENTE','Pendiente')])

    submit = SubmitField("Crear Cuenta")

class EditForm3(Form):
    email = StringField('Correo Eléctronico', [validators.DataRequired(message='Ingrese email'), validators.Email(), validators.Length(min=6, max=35)])
    password = PasswordField('Nueva Contraseña', [validators.DataRequired(),validators.EqualTo('confirm', message='Las contraseñas deben coincidir')])
    estado= SelectField('Estado de la cuenta', choices=[('ACTIVA','ACTIVA'),('INACTIVA','INACTIVA'),('BANEADA','BANEADA'),('PENDIENTE','PENDIENTE')])
    submit= SubmitField("Guardar Cambios")

class EditForm2(Form):
    email = StringField('Correo Eléctronico', [validators.DataRequired(message='Ingrese email'), validators.Email(), validators.Length(min=6, max=35)])
    password = PasswordField('Nueva Contraseña', [validators.DataRequired(),validators.EqualTo('confirm', message='Las contraseñas deben coincidir')])
    nombre= StringField('Nombre', [validators.DataRequired(),  validators.Length(min=3, max=35)])
    apellido= StringField('Apellido', [validators.DataRequired(), validators.Length(min=2, max=35)])
    rut= StringField('Rut', [validators.DataRequired(), validators.Length(min=6, max=13)])
    estado= SelectField('Estado de la cuenta', choices=[('ACTIVA','ACTIVA'),('INACTIVA','INACTIVA'),('BANEADA','BANEADA'),('PENDIENTE','PENDIENTE')])
    

    submit= SubmitField("Guardar Cambios")

class EditForm1(Form):
    email = StringField('Correo Eléctronico', [validators.DataRequired(message='Ingrese email'), validators.Email(), validators.Length(min=6, max=35)])
    password = PasswordField('Nueva Contraseña', [validators.DataRequired(),validators.EqualTo('confirm', message='Las contraseñas deben coincidir')])
    estado= SelectField('Estado de la cuenta', choices=[('ACTIVA','ACTIVA'),('INACTIVA','INACTIVA'),('BANEADA','BANEADA'),('PENDIENTE','PENDIENTE')])

    submit= SubmitField("Guardar Cambios")



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


