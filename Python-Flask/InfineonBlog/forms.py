from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField

# validators to check that the form is filled up correctly during registration
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
	# Validators to check that the input is correct.
	username = StringField('Username', validators=[DataRequired(),Length(min=2, max=20)]) 
	email = StringField('Email', validators=[DataRequired(), Email()]) 
	password = PasswordField('Password', validators=[DataRequired()])
	confirm_password = PasswordField('Confirm Password', validators=[DataRequired(),EqualTo('password')])
	submit = SubmitField('Sign up')


class LoginForm(FlaskForm):
	email = StringField('Email', validators=[DataRequired(), Email()]) 
	password = PasswordField('Password', validators=[DataRequired()])
	remember = BooleanField('Remember Me')
	submit = SubmitField('Login')
