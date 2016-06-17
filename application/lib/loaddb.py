from application import application, db
from application.lib.parser import SheetParser
from config import config_path
from application.entry.models import Entry

import datetime
import warnings

from openpyxl import load_workbook

from application.entry.models import *

class LoadDb():
  @staticmethod
  def load():
    # Refresh the database
    db.drop_all()
    db.create_all()

    with warnings.catch_warnings():
      warnings.simplefilter('ignore')
      # This throws a warning about a named ranged ... we don't care 
      workbook = load_workbook(filename=application.config['QASSIGNMENTS_FILE_URI'], read_only=True)

    sheet = workbook['q Assignments']

    parser = SheetParser(sheet)
    for data in parser.parse():
      entry = Entry(*data)
      db.session.add(entry)

    db.session.commit()