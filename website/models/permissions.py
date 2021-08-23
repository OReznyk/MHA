from ..extensions import db

class Permissions(db.Model):
    id=db.Column("id", db.Integer(), primary_key=True)
    permission=db.Column(db.String(50), unique=True)

    def __repr__(self):
        return f"{self.permission}"
