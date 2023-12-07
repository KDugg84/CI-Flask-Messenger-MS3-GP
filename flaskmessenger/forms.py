from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskmessenger.models import User


class RegistrationForm(FlaskForm):
    # username attribute of the Stringfield class
    username = StringField('Username', validators=[
                        DataRequired(), Length(min=2, max=20)])

    # email attribute of the Stringfield class
    email = StringField('Email', validators=[DataRequired(), Email()])

    # password attribute of Password class
    password = PasswordField('Password', validators=[DataRequired()])

    # password confirmation attribute of Password class
    confirm_password = PasswordField(
        'Confirm Password', validators=[DataRequired(), EqualTo('password')])

    submit = SubmitField('Sign Up Here')

    # custom validations to avoid duplicating users account details
    def validate_username(self, username):
        # conditional to query the database if user's name already exists
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username already exists! Please choose a different one.')


    def validate_email(self, email):
        # conditional to query the database if user's email already exists
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email already exists! Please choose a different one.')        


class LoginForm(FlaskForm):
    # login using email address
    email = StringField('Email', validators=[DataRequired(), Email()])

    password = PasswordField('Password', validators=[DataRequired()])

    # remember cookie to keep users logged in after browser is closed
    remember = BooleanField('Remember Me')

    submit = SubmitField('Login Here')