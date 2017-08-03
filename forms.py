from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length

#Form has been deprecated
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired('Username is required.'), Length(min=8, max=32)])
    password = PasswordField('Password', validators=[InputRequired('Password is required.')])

class RegisterForm(FlaskForm):
    username = StringField('username', validators=[InputRequired('Username is required!'), Length(min=8, max=32)])
    password = PasswordField('password', validators=[InputRequired('Password is required!')])
    rechaptcha = RecaptchaField()
