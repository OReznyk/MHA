from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

DB_NAME = "database.db"

app = Flask(__name__)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
Bootstrap(app)

def create_app():
    ## TODO: change before production
    app.config['SECRET_KEY'] = '432i5oj43n54k2SLtnfk53425erwfjoj43jti52joJeflwGT'
    app.config['SQLACHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

    db.init_app(app)
    # importing blueprints
    from .views import views
    from .auth import auth

    # register blueprints
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app
