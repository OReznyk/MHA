from flask_wtf import FlaskForm
from sqlalchemy.exc import SQLAlchemyError
from wtforms import StringField, PasswordField, BooleanField, SelectField, SubmitField, TextAreaField, FloatField
from wtforms.validators import InputRequired, Email, Length, EqualTo, ValidationError
from wtforms.fields.html5 import DateField
from datetime import date
from flask_login import current_user
from website.models.user import User
from website.models.permissions import Permissions
from website.models.gender import Gender


class LoginForm(FlaskForm):
    email = StringField('אימייל', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    password = PasswordField('סיסמה', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('תזכור אותי')
    submit = SubmitField('להכנס')


class RegistrationForm(FlaskForm):
    genderList = ''
    permissionsList = ''
    try:
        genderList = Gender.query.all()
        permissionsList = Permissions.query.all()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
        pass

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


class UpdateAccountForm(FlaskForm):
    genderList = ''
    permissionsList = ''
    try:
        genderList = Gender.query.all()
        permissionsList = Permissions.query.all()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
        pass

    email = StringField('אימייל', validators=[InputRequired(), Email(message='Invalid email'), Length(max=100)])
    firstname = StringField('שם משפחה', validators=[InputRequired(), Length(min=2, max=50)])
    name = StringField('שם פרטי', validators=[InputRequired(), Length(min=2, max=50)])
    gender = SelectField(u'מין', choices=genderList)
    birthdate = DateField('תאריך לידה', default=date.today())
    permissions = SelectField(u'הרשאות', choices=permissionsList)
    submit = SubmitField('עדכון')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('שמירה נכשלה: משתמש קיים')


class ArticleForm(FlaskForm):
    title = StringField('כותרת', validators=[InputRequired(), Length(min=2, max=150)])
    content = TextAreaField('תוכן', validators=[InputRequired(), Length(min=5, max=150000)])
    submit = SubmitField('שמירה')


class QuestionForm(FlaskForm):
    questionsTypesList = ['אמריקאית', 'פתוחה']
    question = StringField('שאלה', validators=[InputRequired(), Length(min=2, max=250)])
    weight = FloatField('משקל %', validators=[InputRequired(), Length(min=2, max=150)])
    type = SelectField(u'סוג שאלה', choices=questionsTypesList)


class AnswerForm(FlaskForm):
    answer = TextAreaField('תשובה', validators=[InputRequired(), Length(min=2, max=250)])
    weight = FloatField('נכונות %', validators=[InputRequired(), Length(min=2, max=150)])


