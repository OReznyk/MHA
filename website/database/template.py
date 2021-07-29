from . import db

class Template(db.Model):
        _id = db.Column("id", db.Integer, primary_key=True)
        title = db.Column(db.String(150))
        creation_date = db.Column(db.DateTime(timezone=true), default=func.now())
        #TODO: change content val
        content = db.Column(db.String(150), nullable=False)
        author = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

        #TODO: add content val
    def __repr__(self):
        return f"Template('{self.title}', '{self.author}', '{self.creation_date}')"
