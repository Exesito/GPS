from wtforms import Form, SubmitField, StringField, PasswordField, BooleanField, validators
from wtforms import EmailField  
class RegisterForm(Form):
    
    #username = StringField('', [validators.Length(min=4, max=25)])
    email = StringField('Correo Eléctronico', [validators.Length(min=6, max=35)])
    password = PasswordField('Nueva Contraseña', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Las contraseñas deben coincidir')
    ])
    confirm = PasswordField('Repite contraseña')
    submit = SubmitField("Crear Cuenta")


class LoginForm(Form):
    email=EmailField('Correo electrónico',[validators.DataRequired(), validators.Email(), validators.Length(min=6, max=35)])
    password= PasswordField('Contraseña')
    #remember_me = BooleanField('Mantener conectado')

    submit=SubmitField('Iniciar sesión')