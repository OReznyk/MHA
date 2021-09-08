from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_login import login_required, current_user
from website.forms import UpdateAccountForm
from website.models.gender import Gender
from website.models.permissions import Permissions
from website.models.research import Research
from website.models.user import User
from ..extensions import db

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template('index.html')


@views.route('/builder')
def builder():
    return render_template("template_builder.html")


@views.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template("contact_us.html")


@views.route('/about')
def about():
    return render_template("about.html")


@views.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    # if user has no permission_confirmation -> it`s regular user
    table_name = 'מחקרים למילוי'
    table = Research.query.filter_by()
    # else
    if current_user.permission_confirmation:
        perm = "מנהל"
        if current_user.permission == perm:
            table_name = 'משתמשים לאישור הרשאות'
            table = User.query.all()
        elif current_user.permission == 'חוקר' or current_user.permission == 'עוזר מחקר':
            return render_template("dashboard.html", value=Research.query.filter_by(researchers=User.query.filter_by(id=current_user.id).first().researches).all())
        else:
            flash('הרשאות לא הוגדרו', 'error')

    return render_template("dashboard.html", table=table, table_name=table_name)


@views.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    if current_user.is_authenticated:
        user = current_user
        form = UpdateAccountForm()
        if form.validate_on_submit():
            current_user.first_name = form.firstname.data
            current_user.second_name = form.name.data
            current_user.email = form.email.data
            current_user.birth_date = form.birthdate.data
            g = db.session.query(Gender).filter_by(gender=form.gender.data).first()
            g.users.append(user)
            if current_user.permission != form.permissions.data:
                if form.permissions.data == "נחקר":
                    current_user.permission_confirmation = True
                else:
                    current_user.permission_confirmation = False
                p = Permissions.query.filter_by(permission=form.permissions.data).first()
                p.users.append(user)
            db.session.commit()
            flash('שינויים נשמרו בהצלחה', 'success')
        elif request.method == 'GET':
            form.firstname.data = current_user.first_name
            form.name.data = current_user.second_name
            form.email.data = current_user.email
            form.birthdate.data = current_user.birth_date
            form.gender.data = current_user.gender
            form.permissions.data = current_user.permission
        return render_template("profile.html", user=user, form=form)
    else:
        flash('משתמש לא מחובר', 'error')
        return redirect(url_for('auth.login'))

'''
def delete_user():
    if "user" in session:
        User.query.filter_by(id=session["user"].id).delete()
        flash ('משתמש נמחק בהצלחה', 'success')
        return redirect(url_for("view/home"))
'''
