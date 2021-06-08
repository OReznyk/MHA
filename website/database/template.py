from . import db

class Template(db.Model):




    
          def __init__(self, creator, creation_date, creation_month, creation_year,
                        file):
              self.creator = creator
              self.creation_date = creation_date
              self.creation_month = creation_month
              self.creation_year = creation_year
              self.file = file
