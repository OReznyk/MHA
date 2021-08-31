import click
from flask.cli import with_appcontext
from .extensions import db, bcrypt


@click.command(name='create_tables')
@with_appcontext
def create_tables():

    from website.models.answer import Answer
    from website.models.article import Article
    from website.models.gender import Gender
    from website.models.message import Message
    from website.models.permissions import Permissions
    from website.models.question import Question
    from website.models.research import Research
    from website.models.response import Response
    from website.models.role import Role
    from website.models.template import Template
    from website.models.user import User
    #from website.models.participants import Participants

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
    '''gen = db.session.query(Gender).filter_by(gender="אחר").first()
    #perm = Permissions.query.filter_by(permission="מהנל")'''
    #TODO: filled permission & gender ids by hand so need to change it
    user = User(email="admin@t.t", first_name="מנהל", second_name="מנהל", gender=3, permission=4, permission_confirmation=True, password=hashed_pwd)
    db.session.add(user)

    db.session.commit()

