from flask import Blueprint, render_template, flash, request, redirect, url_for
from website.forms import RegistrationForm, LoginForm
from ..extensions import db, bcrypt
from website.models.user import User
from website.models.gender import Gender
from website.models.permissions import Permissions
from flask_login import login_user, logout_user, current_user, login_required

auth = Blueprint('auth', __name__)

'''
    Login function redirects to dashboard.html after authentication
'''


@auth.route('/login', methods=['GET', 'POST'])
def login():
    # if user already logged in -> logout to login
    if current_user.is_authenticated:
        flash('חייבים להתנתק בכדי להכנס מחדש', 'error')
        return redirect(url_for("views.dashboard"))
    else:
        form = LoginForm()
        if form.validate_on_submit():
            # Get user from db
            user = User.query.filter_by(email=form.email.data).first()
            # Checking pwd
            if user and bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                #session.permanent = True
                #session['user'] = user
                # if user get here from page that needed authentication -> redirect to that page
                next_page = request.args.get('next')
                return redirect(next_page) if next_page else redirect(url_for('views.dashboard'))
            else:
                flash('הוכנסו נתונים לא נכונים', 'error')
    return render_template('login.html', form=form)


'''
    Signup function redirects to:
                1. dashboard.html if user is_authenticated
                2. login.html if user created successfuly
'''


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        flash('בבקשה תתנתקו לצורך רישום משתמש חדש', 'error')
        return redirect(url_for("views.dashboard"))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pwd = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        # TODO: check permissions: create regular user for all types of permissions
        # if not regular permission ->  flash msg as: user created & send for permission approval
        user = User(email=form.email.data, first_name=form.firstname.data,
                        second_name=form.name.data, birth_date=form.birthdate.data, password=hashed_pwd)
        if form.permissions.data == "נחקר":
            user.permission_confirmation = True
        # Saving user to db
        db.session.add(user)
        g = db.session.query(Gender).filter_by(gender=form.gender.data).first()
        p = Permissions.query.filter_by(permission=form.permissions.data).first()
        g.users.append(user)
        p.users.append(user)
        db.session.commit()
        flash('משתמש נוצר בהצלחה', 'success')
        # TODO: send email verificathion if needed
        # TODO: redirect to verification page/popup?
        return redirect(url_for("auth.login"))

    return render_template('signup.html', form=form)


'''
    Logout function redirects to home page
'''


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("views.home"))
