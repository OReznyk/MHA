from ..extensions import db


class Permissions(db.Model):
    id = db.Column("id", db.Integer(), primary_key=True)
    permission = db.Column(db.String(50), unique=True)
    users = db.relationship('User', backref='permission', lazy=True)

    def __repr__(self):
        return self.permission
