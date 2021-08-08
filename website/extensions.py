from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from flask_bootstrap import Bootstrap
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
login_manager = LoginManager()
bcrypt = Bcrypt()
bootstrap = Bootstrap()
