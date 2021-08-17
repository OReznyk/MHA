import click
from flask.cli import with_appcontext
from .extensions import db, bcrypt

from website.models.user import User
from website.models.permissions import Permissions
from website.models.gender import Gender


@click.command(name='create_tables')
@with_appcontext
def create_tables():
    db.create_all()

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

    db.session.commit()
        # Default init for admin #
    #TODO: change in prod mode
    hashed_pwd = bcrypt.generate_password_hash("12345678").decode('utf-8')
    #gen = Gender.query.filter_by(gender="אחר").first()
    #perm = Permissions.query.filter_by(permission="מהנל").first()
    user = User(email="admin@t.t", first_name="מנהל",
                    second_name="מנהל",
                    gender="אחר", permission="מנהל", password=hashed_pwd)
    db.session.add(user)

    db.session.commit()

