from flask import Blueprint, render_template, flash

views = Blueprint('views', __name__)

@views.route('/')
def home():
    flash('zdfsdafaffga', category = 'info')
    return render_template('index.html')

@views.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    return render_template("dashboard.html")
