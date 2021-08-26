from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session
from flask_bootstrap import Bootstrap
from flask_bcrypt import Bcrypt
from flask_wtf.csrf import CSRFProtect

db = SQLAlchemy()
session = Session()
login_manager = LoginManager()
bcrypt = Bcrypt()
bootstrap = Bootstrap()
csrf = CSRFProtect()
