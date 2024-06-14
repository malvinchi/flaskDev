from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo

#create the Registration Form
class RegistrationForm(FlaskForm):
    username=StringField("Username", validators=[DataRequired(), Length(min=8, max=20)])
    email=EmailField("Email", validators=[DataRequired()])
    password=PasswordField("Password", validators=[DataRequired(), Length(min=8, max=12)])
    confirm_password=PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password")])
    submit=SubmitField("Register Here")


# create login form
class LoginForm(FlaskForm):
    email=EmailField("Email", validators=[DataRequired()])
    password=PasswordField("Password", validators=[DataRequired()])
    submit=SubmitField(" Login Here")
