from flask import Blueprint, render_template, flash
from flask_login import login_required
from extentions import app, db, bcrypt
from website.database.user import User

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('index.html')

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
    return render_template("dashboard.html", value = User.query.all())

@views.route('/profile')
@login_required
def profile():
    return render_template("profile.html")

def delete_user():
    if "user" in session:
        User.query.filter_by(id=session["user"].id).delete()
        flash ('משתמש נמחק בהצלחה', 'success')
        return redirect(url_for("view/home"))
