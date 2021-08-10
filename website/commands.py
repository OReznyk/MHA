import click
from flask.cli import with_appcontext

from .extensions import db
from website.database.user import User
from website.database.permissions import Permissions
from website.database.gender import Gender


@click.command(name='create_tables')
@with_appcontext
def create_tables():
    '''
     # Default init for permissions #
    perm = ["נחקר", "חוקר", "עוזר מחקר", "מהנל"]
    for p in perm:
        permission = Permissions(permission = p)
        db.session.add(permission)

    # Default init for gender #
    gen = ["זכר", "נקבה", " אחר"]
    for g in gen:
        gender = Gender(gender=g)
        db.session.add(gender)

    '''

    db.create_all()
    #db.session.commit()
