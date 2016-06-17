from application import application, db
from config import config_path
import datetime

from application.lib.loaddb import LoadDb

application.config.from_object(config_path)

LoadDb.load()