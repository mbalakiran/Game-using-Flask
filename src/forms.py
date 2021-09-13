from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField,SubmitField, BooleanField
from wtforms.validators import DataRequired, ValidationError,Length, Email, EqualTo
from src.models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):

        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username already Exits')


    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email already Exits')

class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class PlayGame(FlaskForm):
    level = StringField('Level', validators=[DataRequired(), Length(min=1, max=3)])
    score = IntegerField('Your Score')
    submit = SubmitField('Submit Score')