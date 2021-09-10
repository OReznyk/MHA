from website import create_app
from os import environ
"""
created by Olga Reznyk
"""


app = create_app(environ.get('DevConfig'))
if __name__ == '__main__':
    # TODO: WARNING!!!! Turn off debug option before production !!!!!!!
    app.run()
