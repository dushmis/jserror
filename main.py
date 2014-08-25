#!/usr/bin/env python

import webapp2
from google.appengine.api import mail
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp.mail_handlers import InboundMailHandler

from google.appengine.ext import ndb

from google.appengine.ext import db

from google.appengine.ext import blobstore
from google.appengine.api import files

from google.appengine.api import users


class jserror(db.Model):
  err_ = db.StringProperty()
  content_ = db.TextProperty()
  page_ = db.StringProperty()
  domain_ = db.StringProperty()
  ip_ = db.StringProperty()
  date = db.DateTimeProperty(auto_now_add=True)

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
      self.response.write(ddr.key())

class AdminHandler(webapp2.RequestHandler):
  def get(self):
    user = users.get_current_user()
    if user:
      self.response.headers['Content-Type'] = 'text/html'
      greeting = ('Welcome, %s! (<a href="%s">sign out</a>)' %
                        (user.nickname(), users.create_logout_url('/')))
      self.response.write(greeting)
      q = db.GqlQuery("select * from jserror order by date DESC ")
      #q.order("-date")
      results=q.fetch(limit=100)
      self.response.write("<div style='padding-bottom:10px;'> --- </div>")
      for jserror in results:
        self.response.write("<div>%s - %s</div>" % (jserror.err_,jserror.date))
    else:
      self.redirect(users.create_login_url(self.request.uri))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/_admin', AdminHandler)
], debug=True)
