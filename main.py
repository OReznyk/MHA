from website import create_app

"""
created by Olga Reznyk
"""

app = create_app()

if __name__ == '__main__':
    # TODO: Turn off debug option before production
    app.run( debug  = True)
