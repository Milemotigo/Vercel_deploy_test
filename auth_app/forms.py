from flask import request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo
from wtforms import ValidationError
from .models import User

class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired(), Length(min=15, max=23)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember me', default=False)
    submit = SubmitField('Login')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password', message='passwords must match!')])
    email = EmailField('Email', validators=[DataRequired(), Length(min=6, max=200)])
    remember = BooleanField('Remember me', default=False)
    submit = SubmitField('Create Account')

    def validate_email(self, email):
        email = User.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError('email already exists')

