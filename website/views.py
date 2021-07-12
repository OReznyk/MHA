from flask import Blueprint, render_template, flash

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('index.html')

@views.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    return render_template("dashboard.html")

@views.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template("contact_us.html")

@views.route('/about')
def about():
    return render_template("about.html")
