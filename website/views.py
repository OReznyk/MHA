from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('index.html')

@views.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")

@views.route('/ContactResearch')
def ContactResearch():
    return render_template("ContactResearch.html")
