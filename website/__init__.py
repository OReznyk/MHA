from flask import Flask
from .commands import *
import config
from .extensions import db, bootstrap, bcrypt, login_manager, csrf, session
from website.models import questioner, question, answer, research, gender, user, article, message, permissions
from website.models import research_participants, role, response
# import models.questioner
# import models.question
# import models.gender
# import models.user
# import models.answer
# import models.article

def create_app(config_name):
    ## create & configure the app
    app = Flask(__name__)

    if config_name is None:
        app.config.from_object(config.BaseConfig)
    else:
        app.config.from_object(config_name)

    app.app_context().push()
    db.init_app(app)
    bootstrap.init_app(app)
    session.init_app(app)
    bcrypt.init_app(app)
    csrf.init_app(app)

    login_manager.init_app(app)

    # commands initialization
    app.cli.add_command(create_tables)
    app.cli.add_command(drop_db)
    app.cli.add_command(reset_db)
    app.cli.add_command(add_default_gender)
    app.cli.add_command(add_default_permissions)
    app.cli.add_command(add_default_admin)

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
