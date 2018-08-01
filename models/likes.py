from google.appengine.ext import db


class Likes(db.Model):
    name = db.StringProperty(required=True)
    post_id = db.IntegerProperty()
    comment_id = db.IntegerProperty()
    created = db.DateTimeProperty(auto_now_add=True)
    last_modified = db.DateTimeProperty(auto_now=True)
