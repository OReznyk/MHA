from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname('website'))
load_dotenv(path.join(basedir, '.env'))


class BaseConfig:
    """Base config."""
    DB_SERVER = 'localhost'
    SECRET_KEY = environ.get('SECRET_KEY') or \
        '\xfd{H\xe5<\x95\xf9\xe3\x96.5\xd1\x01O<!\xd5\xa2\xa0\x9fR"\xa1\xa8'
    FLASK_SECRET = SECRET_KEY
    SQLALCHEMY_DATABASE_URI = environ.get('SQLALCHEMY_DATABASE_URI')
    SESSION_COOKIE_NAME = environ.get('SESSION_COOKIE_NAME')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CSRF_ENABLED = True
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'
    SESSION_TYPE = 'filesystem'
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'None'
    WTF_CSRF_ENABLED = environ.get('WTF_CSRF_ENABLED')


class ProdConfig(BaseConfig):
    DB_SERVER = ''
    SECRET_KEY = environ.get('SECRET_KEY') or \
        '\xfd{H\xe5<\x95\xf9\xe3\x96.5\xd1\x01O<!\xd5\xa2\xa0\x9fR"\xa1\xa8'
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = environ.get('SQLALCHEMY_DATABASE_URI')  or \
        'sqlite:///' + path.join(basedir, 'db.sqlite')


class DevConfig(BaseConfig):

    SECRET_KEY = environ.get('SECRET_KEY') or \
        'rrehgritruehgokfakfpoewrkgwo'
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True
    DB_SERVER = 'localhost'
    SQLALCHEMY_DATABASE_URI = environ.get('SQLALCHEMY_DATABASE_URI')  or \
        'sqlite:///' + path.join(basedir, 'db.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    WTF_CSRF_SECRET_KEY = SECRET_KEY

config = {
    'dev': DevConfig,
    'prod': ProdConfig,
    'default': DevConfig,
}
