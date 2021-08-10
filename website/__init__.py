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

        from website.database.user import User
        from website.database.permissions import Permissions
        from website.database.gender import Gender

        # Default init for permissions #
        perm = ["נחקר", "חוקר", "עוזר מחקר", "מהנל"]
        for p in perm:
            permission = Permissions(permission = p)
            db.session.add(permission)

        # Default init for gender #
        gen = ["זכר", "נקבה"," אחר"]
        for g in gen:
            gender = Gender(gender = g)
            db.session.add(gender)

        db.create_all()
        db.session.commit()



def create_app():
    ## TODO: change before production
    app.config['SECRET_KEY'] = '432i5oj43n54k2SLtnfk53425erwfjoj43jti52joJeflwGT'
    app.config['SQLACHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

    login_manager.init_app(app)
    # creating database
    init_database()
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
