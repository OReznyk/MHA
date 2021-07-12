from flask import Blueprint, render_template, flash, request, redirect, url_for, session
from flask_bootstrap import Bootstrap
from website.forms import RegistrationForm, LoginForm
from website import app, db, bcrypt
from website.database.user import User
from flask_login import login_user

from flask_sqlalchemy import SQLAlchemy

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Get user from db
        user = User.query.filter_by(email=form.email.data).first()
        # Checking pwd
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('views.dashboard'))
        else:
            flash ('הוכנסו נתונים לא נכונים', 'error')
    return render_template('login.html', form=form)


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pwd = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        #TODO: check permissions: create regular user for all types of permissions
        # if not regular permission -> send to admin for change + flash msg as: user created & send for permission approval
        gender = form.gender.data
        permission = form.permissions.data
        #TODO: set id's for gender & permissions
        user = User(email = form.email.data , first_name = form.firstname.data,
                            second_name = form.name.data, birth_date = form.birthdate.data,
                            gender = form.gender.data, permission = form.permissions.data, password = hashed_pwd)
        # Saving user to database
        db.session.add(user)
        db.session.commit()
        flash ('משתמש נוצר בהצלחה', 'success')
        #TODO: send email verificathion if needed
        #TODO: redirect to verification page/popup?
        return redirect(url_for("auth.login"))

    return render_template('signup.html', form=form)
