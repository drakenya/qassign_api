from application import db

class Entry(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  
  date = db.Column(db.Date)
  initials = db.Column(db.String(8))
  part_code = db.Column(db.String(8))

  def __init__(self, date, initials, part_code):
    self.date = date
    self.initials = initials
    self.part_code = part_code