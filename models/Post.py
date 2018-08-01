from google.appengine.ext import db
from user import User
from handlers.utils import Utils


class Post(db.Model):
    author = db.ReferenceProperty(User)
    subject = db.StringProperty(required=True)
    content = db.TextProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)
    last_modified = db.DateTimeProperty(auto_now=True)
    # likes = db.IntegerProperty(default=0)
    LikersArray = db.StringListProperty()

    @property
    def likes(self):
        # return the number of users in the array who liked the post
        return len(self.LikersArray)

    @property
    def comments(self):
        # return all Comments for this post
        comments = db.GqlQuery("select * from Comment")
        return comments

    def render(self):
        self._render_text = self.content.replace('\n', '<br>')
        return Utils().render_str("post.html", p=self)
