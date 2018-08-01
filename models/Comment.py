from google.appengine.ext import db
from models.Post import Post


class Comment(db.Model):
    comment = db.TextProperty()
    name = db.StringProperty()
    added = db.DateTimeProperty(auto_now_add=True)
    created = db.DateTimeProperty(auto_now=True)
    last_modified = db.DateTimeProperty(auto_now=True)
    post_id = db.ReferenceProperty(Post)
    postId = db.IntegerProperty()
