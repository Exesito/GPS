from wtforms import Form, SubmitField, SelectField, StringField, PasswordField, BooleanField, validators, IntegerField
  
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
    email=StringField('Correo electrónico',[validators.Length(min=6, max=35)])
    password= PasswordField('Contraseña')
    #remember_me = BooleanField('Mantener conectado')
    

    submit=SubmitField('Iniciar sesión')


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