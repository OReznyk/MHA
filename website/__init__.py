from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from .commands import create_tables
import config
from .extensions import db, bootstrap, bcrypt, login_manager, csrf, sess

db = SQLAlchemy()
def create_app(config_name):
    ## create & configure the app
    app = Flask(__name__)
    app.app_context().push()

    if config_name is None:
        app.config.from_object(config.BaseConfig)
    else:
        app.config.from_object(config_name)

    sess.init_app(app)
    db.init_app(app)
    bcrypt.init_app(app)
    csrf.init_app(app)
    bootstrap.init_app(app)
    login_manager.init_app(app)
    app.cli.add_command(create_tables)

    # importing blueprints
    from website.routes.views import views
    from website.routes.auth import auth

    # register blueprints
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    # login Manager configurations
    login_manager.login_view = 'auth.login'
    login_manager.login_message = u"תכנסו בבקשה"
    login_manager.login_message_category = 'info'
    return app

# models configurations

