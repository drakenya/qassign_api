from flask import Flask
from flask.ext.restful import Api
from flask.ext.sqlalchemy import SQLAlchemy

application = Flask(__name__)
api = Api(application)
db = SQLAlchemy(application)

from application.entry import views as _
from application.update import views as _