from flask import Blueprint, render_template, flash, request, redirect, url_for
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from wtforms.fields.html5 import DateField
from wtforms import StringField, PasswordField, BooleanField, SelectField
from wtforms.validators import InputRequired, Email, Length
from datetime import date

auth = Blueprint('auth', __name__)

class LoginForm(FlaskForm):
    email = StringField('אימייל', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    password = PasswordField('סיסמה', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('תזכור אותי')


class RegisterForm(FlaskForm):
    permissionsList = ["נחקר", "חוקר", "עוזר מחקר", "מהנל"]
    genderList = ["זכר", "נקבה"," אחר"]

    email = StringField('אימייל', validators=[InputRequired(), Email(message='Invalid email'), Length(max=100)])
    firstname = StringField('שם משפחה', validators=[InputRequired(), Length(min=2, max=50)])
    name = StringField('שם פרטי', validators=[InputRequired(), Length(min=2, max=50)])
    gender = SelectField(u'מין', choices=genderList)
    birthdate = DateField('תאריך לידה', default=date.today())
    name = StringField('שם פרטי', validators=[InputRequired(), Length(min=2, max=15)])
    password = PasswordField('סיסמה', validators=[InputRequired(), Length(min=8, max=50)])
    verification = PasswordField('אימות סיסמה', validators=[InputRequired(), Length(min=8, max=50)])
    permissions = SelectField(u'הרשאות', choices=permissionsList)
    remember = BooleanField('תזכור אותי')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # TODO: for POST request get & check users data -> if ok redirect to user's page
        return redirect(url_for("user.html"))
    else:
        # for GET request return page
        return render_template('login.html', form=form)


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()
    if form.validate_on_submit():
        ## TODO: flashing not working yet
        if form['password'] != form['verification'] :
            flash('סיסמאות לא זהות', 'error')
        else:
            #TODO: check permissions: create regular user for all types of permissions
            # if not regular permission -> send to admin for change + flash msg as: user created & send for permission approval
            flash ('משתמש נוצר', 'success')
            return redirect(url_for("user.html"))
    return render_template('signup.html', form=form)
