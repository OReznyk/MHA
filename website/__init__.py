from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

login_manager = LoginManager(app)

# database configurations
DB_NAME = "database.db"

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
Bootstrap(app)


def init_database():
        #from website.database.answer import Answer
        #from website.database.article import Article
        #from website.database.gender import Gender
        #from website.database.permissions import Permission
        #from website.database.question import Question
        #from website.database.research import Research
        #from website.database.template import Template
        from website.database.user import User

        db.create_all()
        db.session.commit()
        return 0

init_database()

def create_app():
    ## TODO: change before production
    app.config['SECRET_KEY'] = '432i5oj43n54k2SLtnfk53425erwfjoj43jti52joJeflwGT'
    app.config['SQLACHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

    login_manager.init_app(app)
    # creating database
    init_database()
    # importing blueprints
    from .views import views
    from .auth import auth

    # register blueprints
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    # login Manager configurations
    login_manager.login_view = 'auth.login'
    login_manager.login_message = u"תכנסו בבקשה"
    login_manager.login_message_category = 'info'

    return app
