from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SelectField, SubmitField
from wtforms.validators import InputRequired, Email, Length, EqualTo, ValidationError
from wtforms.fields.html5 import DateField
from datetime import date
from website.models.user import User
from website.models.permissions import Permissions
from website.models.gender import Gender


class LoginForm(FlaskForm):
    email = StringField('אימייל', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    password = PasswordField('סיסמה', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('תזכור אותי')
    submit = SubmitField('להכנס')


class RegistrationForm(FlaskForm):
    # TODO: change it to pull from table
    genderList = Gender.query.all()
    permissionsList = Permissions.query.all()

    email = StringField('אימייל', validators=[InputRequired(), Email(message='Invalid email'), Length(max=100)])
    firstname = StringField('שם משפחה', validators=[InputRequired(), Length(min=2, max=50)])
    name = StringField('שם פרטי', validators=[InputRequired(), Length(min=2, max=50)])
    gender = SelectField(u'מין', choices=genderList)
    birthdate = DateField('תאריך לידה', default=date.today())
    password = PasswordField('סיסמה', validators=[InputRequired(), Length(min=8, max=50)])
    verification = PasswordField('אימות סיסמה', validators=[InputRequired(), EqualTo('password')])
    permissions = SelectField(u'הרשאות', choices=permissionsList)
    remember = BooleanField('תזכור אותי')
    submit = SubmitField('להרשם')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('הרשמה נכשלה: משתמש קיים')
