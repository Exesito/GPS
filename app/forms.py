from wtforms import Form, SubmitField, StringField, PasswordField, validators
  
class RegisterForm(Form):
    
    #username = StringField('', [validators.Length(min=4, max=25)])
    email = StringField('Correo Eléctronico', [validators.Length(min=6, max=35)])
    password = PasswordField('Nueva Contraseña', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Las contraseñas deben coincidir')
    ])
    confirm = PasswordField('Repite contraseña')
    submit = SubmitField("Crear Cuenta")