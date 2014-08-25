#!/usr/bin/env python

import webapp2
from google.appengine.api import mail
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp.mail_handlers import InboundMailHandler

from google.appengine.ext import ndb

from google.appengine.ext import blobstore
from google.appengine.api import files

class jserror(ndb.Model):
  err_ = ndb.StringProperty()
  content_ = ndb.TextProperty()
  page_ = ndb.StringProperty()
  domain_ = ndb.StringProperty()
  ip_ = ndb.StringProperty()
  date = ndb.DateTimeProperty(auto_now_add=True)

class MainHandler(webapp2.RequestHandler):
  def get(self):
    self.response.write("hey?")
  def post(self):
    self.response.headers.add_header("Access-Control-Allow-Origin", "*")
    if self.request.get("er"):
      import json
      b=json.loads(self.request.get("er"))
      ddr=jserror(err_=b["0"],content_=str(b),page_=b["1"],domain_="")
      ddr.put()
      #Access-Control-Allow-Origin:*
      self.response.write(ddr.key)

class AdminHandler(webapp2.RequestHandler):
  def get(self):
    self.response.write("hey...?")

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/_admin', AdminHandler)
], debug=True)
