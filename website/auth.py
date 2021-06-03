from flask import Blueprint, render_template, redirect, url_for
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length

auth = Blueprint('auth', __name__)

class LoginForm(FlaskForm):
    email = StringField('אימייל', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    password = PasswordField('סיסמה', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('תזכור אותי')


class RegisterForm(FlaskForm):
    email = StringField('אימייל', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    firstname = StringField('שם משפחהי', validators=[InputRequired(), Length(min=4, max=15)])
    name = StringField('שם פרטי', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('סיסמה', validators=[InputRequired(), Length(min=8, max=80)])
    verification = PasswordField('אימות סיסמה', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('תזכור אותי')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', form=form)


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()
    if form.validate_on_submit():
        return '<h1>New user has been created!</h1>'
    return render_template('signup.html', form=form)
