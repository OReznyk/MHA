from flask import Blueprint, render_template, flash
from flask_login import login_required
from ..extensions import bcrypt
from website.models.user import User
#from auth import current_user

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('index.html')


@views.route('/contactResearch')
def ContactResearch():
    return render_template("ContactResearch.html")

@views.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template("contact_us.html")

@views.route('/about')
def about():
    return render_template("about.html")

@views.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    #TODO: define permissions cond
    permission = Permissions.query.filter_by(id = User.query.filter_by(id=user.id).first().permission).first()
    if(permission == 'מנהל'):
        return render_template("dashboard.html", value = User.query.all())
    elif(permission == 'נחקר'):
        #TODO: return researches user pert-in
        return render_template("dashboard.html", value = Research.query.all())
    elif(permission == 'חוקר' or permission == 'עוזר מחקר'):
        return render_template("dashboard.html", value = Research.query.filter_by(researchers=User.query.filter_by(id=user.id).first().researches).all())
    else: flash('הרשאות לא הוגדרו', 'error')
    return render_template("dashboard.html")

@views.route('/profile')
@login_required
def profile():
    return render_template("profile.html")

@views.route('/builder')
#@login_required
def builder():
    return render_template("template_builder.html")
'''
def delete_user():
    if "user" in session:
        User.query.filter_by(id=session["user"].id).delete()
        flash ('משתמש נמחק בהצלחה', 'success')
        return redirect(url_for("view/home"))
'''
