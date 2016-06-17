from flask import Response, jsonify
from flask.json import dumps
from flask.ext.classy import FlaskView, route
from datetime import date

from application import application, api, db
from application.lib.alchemy import AlchemyEncoder

from application.entry.models import Entry

class EntryView(FlaskView):
  @route('/')
  def index(self):
    return Response(dumps(Entry.query.all(), cls=AlchemyEncoder, indent=2), mimetype='application/json')

  @route('/current')
  def current(self):
    return Response(dumps(Entry.query.filter(Entry.date >= date.today()).all(), cls=AlchemyEncoder, indent=2), mimetype='application/json')

EntryView.register(application)