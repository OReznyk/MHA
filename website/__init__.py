from flask import Flask, redirect, url_for
from flask_bootstrap import Bootstrap

def create_app():
    app = Flask(__name__)
    Bootstrap(app)
    ## TODO: change before production
    app.config['SECRET_KEY'] = 'Thisissupposedtobesecret'

    # importing blueprints
    from .views import views
    from .auth import auth

    # register blueprints
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')





    return app
