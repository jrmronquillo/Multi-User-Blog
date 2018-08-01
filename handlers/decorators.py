from functools import wraps
from google.appengine.ext import db


def blog_key(name='default'):
    return db.Key.from_path('post', name)


def post_exists(function):
    """
    Check to validate post exists, if not report error with 404 page
    """
    @wraps(function)
    def wrapper(self, post_id):
        key = db.Key.from_path("Post", int(post_id), parent=blog_key())
        posts = db.get(key)
        if posts:
            return function(self, post_id, posts)
        else:
            print "Post was not found"
            self.error(404)
            return
    return wrapper


def login_required(func):
    """
    Decorator to confirm user is logged in, otherwise redirects to login page
    """
    def login(self, *args, **kwargs):
        # Redirect to login if user is not logged in, else execute function
        if not self.user:
            self.redirect("/login")
        else:
            func(self, *args, **kwargs)
    return login


def user_logged_in(function):
    """
    Decorator to set user to 'Guest' if user is not logged in"
    """
    @wraps(function)
    def wrapper(self):
        if self.user:
            user = self.user.name
            error = ""
            function(self, user, error)
        else:
            user = 'Guest'
            error = ""
            function(self, user, error)
    return wrapper


def user_owns_post(function):
    """
    Check if user is the same as the post author, do nothing and redirect to
    blog front page.
    """
    @wraps(function)
    def wrapper(self, post_id, posts):
        if self.user.name == posts.author.name:
            function(self, post_id, posts)
        else:
            print posts.author.name
            # print "error in decorator"
            # self.error(404)
            return self.redirect("/blog/?")
    return wrapper


def user_owns_comment(function):
    """
    Check if user is the same as comment author, if not, do nothing and
    redirect toblog front page
    """
    @wraps(function)
    def wrapper(self, comment_id, comment):
        if self.user.name == comment.name:
            function(self, comment_id, comment)
        else:
            return self.redirect("/blog")
    return wrapper


def comment_exists(function):
    """
    Check to validate comment exists, if not report error with 404 page
    """
    @wraps(function)
    def wrapper(self, comment_id):
        key = db.Key.from_path("Comment", int(comment_id))
        comment = db.get(key)
        if comment:
            return function(self, comment_id, comment)
        else:
            print "Comment Post not found"
            self.error(404)
            return
    return wrapper
