from datetime import datetime

class SheetParser():
  sheet = None

  def __init__(self, sheet):
    self.sheet = sheet

  def parse(self):
    initials = self.map_initials()
    parts = self.extract_parts(initials)

    return parts

  def extract_parts(self, initials):
    parts = []
    
    for cell in self.sheet.get_squared_range(self.sheet.min_column, self.sheet.min_row + 1, self.sheet.max_column, self.sheet.max_row):
      # Only parse rows that have a valid date
      if isinstance(cell[0].value, datetime):
        date = cell[0].value
        for key in initials:
          current_value = cell[key]
          for part in self.get_parts(cell[key].value):
            parts.append((date, initials[key], part))

    return parts

  def get_parts(self, value):
    if value == None:
      return []

    parts = value.strip().upper().split()

    invalid_parts = ['XXX']
    valid_parts = [val for val in parts if val not in invalid_parts]

    return valid_parts

  def map_initials(self):
    initials = {}

    for cell in self.sheet.get_squared_range(self.sheet.min_column, self.sheet.min_row, self.sheet.max_column, 1):
      for row in cell:
        if (self.are_initials(row.value)):
          initials[row.column] = row.value

    return initials

  def are_initials(self, initials):
    if isinstance(initials, str) and len(initials) <= 3 and initials.isupper() == True:
      return True

    return False

