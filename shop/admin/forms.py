from wtforms import Form, BooleanField, StringField, PasswordField, validators

class RegistrationForm(Form):
    nombre = StringField('Nombre', [validators.Length(min=4, max=25)])
    correo = StringField('Correo', [validators.Length(min=6, max=35), validators.Email()])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')


    