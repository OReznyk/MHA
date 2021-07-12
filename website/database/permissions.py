from website import db

class Permissions(db.Model):
    _id = db.Column("id", db.Integer(), primary_key=True)
    permission = db.Column(db.String(50), unique=True)

    def __repr__(self):
        return f"Permissions('{self.permission}')"


db.create_all()
db.session.commit()
