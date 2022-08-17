from wtforms import Form, SubmitField, StringField, PasswordField, IntegerField, SelectField,validators
from wtforms import EmailField  
class RegisterForm(Form):
    
    #username = StringField('', [validators.Length(min=4, max=25)])
    email = StringField('Correo Eléctronico', [validators.DataRequired(message='Ingrese email'), validators.Email(), validators.Length(min=6, max=35)])
    password = PasswordField('Nueva Contraseña', [validators.DataRequired(),validators.EqualTo('confirm', message='Las contraseñas deben coincidir')])
    confirm = PasswordField('Repite contraseña', [validators.DataRequired()])
    nombre= StringField('Nombre', [validators.DataRequired(),  validators.Length(min=3, max=35)])
    apellido= StringField('Apellido', [validators.DataRequired(), validators.Length(min=2, max=35)])
    rut= StringField('Rut', [validators.DataRequired(), validators.Length(min=6, max=13)])
    celular=IntegerField('Celular')#,[validators.DataRequired()]
    region=SelectField('Region')
    ciudad=SelectField('Ciudad')
    calle=StringField('Calle', [validators.DataRequired()])
    numero=IntegerField('Número', [validators.DataRequired()])
    #tipo=SelectField('Tipo')

    submit = SubmitField("Crear Cuenta")


class LoginForm(Form):
    email=EmailField('Correo electrónico',[validators.DataRequired(), validators.Email(), validators.Length(min=6, max=35)])
    password= PasswordField('Contraseña')
    #remember_me = BooleanField('Mantener conectado')

    submit=SubmitField('Iniciar sesión')


#class RecoveryForm(Form):
#    email=EmailField()
#    submit=SubmitField('Recuperar acceso')