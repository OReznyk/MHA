from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'Thisissupposedtobesecret!'

class LoginForm(FlaskForm):
    firstname = StringField('שם פרטי', validators=[InputRequired(), Length(min=4, max=15)])
    lastname = StringField('שם משפחה', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('סיסמה', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('תזכור אותי')

class RegisterForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
    verification = StringField('verification', validators=[InputRequired(), Length(max=50)])

@app.route('/')
def index():
    return render_template('index2.html')

@app.route('/user')
def user_main():
    return render_template('user_main.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', form=form)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm
    if form.validate_on_submit():
        return '<h1>New user has been created!</h1>'
    return render_template('signup.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
