from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

# database configurations
DB_NAME = "database.db"
## TODO: change before production
app.config['SECRET_KEY'] = '432i5oj43n54k2SLtnfk53425erwfjoj43jti52joJeflwGT'
app.config['SQLACHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
db = SQLAlchemy(app)

#from website.database.user import User
#db.create_all()
#db.session.commit()

# login Manager configurations
login_manager = LoginManager(app)
login_manager.login_view = 'auth.login'
login_manager.login_message = u"תכנסו בבקשה"
login_manager.login_message_category = 'info'

bcrypt = Bcrypt(app)
Bootstrap(app)

# importing blueprints
from .views import views
from .auth import auth

# blueprints registration
app.register_blueprint(views, url_prefix='/')
app.register_blueprint(auth, url_prefix='/')

'''
def create_app():
    ## TODO: change before production
    app.config['SECRET_KEY'] = '432i5oj43n54k2SLtnfk53425erwfjoj43jti52joJeflwGT'
    app.config['SQLACHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

    login_manager.init_app(app)
    # creating databa
    from website.database.user import User
    db.init_app(app)
    db.create_all()
    db.session.commit()
    # importing blueprints
    from .views import views
    from .auth import auth

    # register blueprints
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app
'''
