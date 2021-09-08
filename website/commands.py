import click
from flask.cli import with_appcontext
from .extensions import db, bcrypt


@click.command(name='create_tables')
@with_appcontext
def create_tables():
    from website.models.answer import Answer
    from website.models.article import Article
    from website.models.message import Message
    from website.models.question import Question
    from website.models.response import Response
    from website.models.role import Role
    from website.models.permissions import Permissions
    from website.models.gender import Gender

    from website.models.research import Research
    from website.models.user import User

    from website.models.questioner import Questioner
    from website.models.research_participants import Participants

    db.create_all()
    if not db.session.commit():
        print('DataBase created')
    else:
        print('Error: DataBase not created')


@click.command(name='add_default_admin')
@with_appcontext
def add_default_admin():
    """ Adding default admin with password '12345678' & email 'admin@t.t' """
    # TODO: change in prod mode
    hashed_pwd = bcrypt.generate_password_hash("12345678").decode('utf-8')
    # TODO: filled permission & gender ids by hand so need to change it
    from website.models.user import User
    from website.models.permissions import Permissions
    from website.models.gender import Gender
    user = User(email="admin@t.t", first_name="מנהל", second_name="מנהל", permission_confirmation=True, password=hashed_pwd)
    db.session.add(user)
    g = db.session.query(Gender).filter_by(gender="אחר").first()
    p = Permissions.query.filter_by(permission="מהנל").first()
    g.users.append(user)
    p.users.append(user)
    db.session.commit()

    print('Initialized default admin')


@click.command(name='add_default_permissions')
@with_appcontext
def add_default_permissions():
    """ Adding default permissions """
    # Default init for permissions
    from website.models.permissions import Permissions
    perm = ["נחקר", "חוקר", "עוזר מחקר", "מנהל"]
    for p in perm:
        permission = Permissions(permission=p)
        db.session.add(permission)
    db.session.commit()

    print('Initialized default permissions')


@click.command(name='add_default_gender')
@with_appcontext
def add_default_gender():
    """ Adding default gender """
    from website.models.gender import Gender
    gen = ["זכר", "נקבה", "אחר"]
    for g in gen:
        gender = Gender(gender=g)
        db.session.add(gender)
    db.session.commit()

    print('Initialized default gender')


@click.command(name='reset_db')
@with_appcontext
def reset_db():
    """ Drops & Creates fresh database"""
    db.drop_all()
    create_tables()
    print('Initialized default db')


@click.command(name='drop_db')
@with_appcontext
def drop_db():
    """ Drops database"""
    if db.drop_all():
        print('Dropped db')
    else:
        print('Problem in db dropping')
