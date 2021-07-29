from flask import Blueprint, render_template, flash
from flask_login import login_required

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('index.html')


@views.route('/ContactResearch')
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
    return render_template("dashboard.html")

@views.route('/profile')
@login_required
def profile():
    return render_template("profile.html")

