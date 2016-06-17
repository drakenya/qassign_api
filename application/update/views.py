from flask import Response
from flask.ext.classy import FlaskView, route

from application import application
from application.lib.loaddb import LoadDb

class UpdateView(FlaskView):
  @route('/', methods=['POST'])
  def index(self):
    LoadDb.load()
    return Response('')

UpdateView.register(application)