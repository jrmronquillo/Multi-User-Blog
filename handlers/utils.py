import hmac
import random
from string import letters
import hashlib
from functools import wraps
from google.appengine.ext import db
import re
import main

SECRET = 'j;;KX;LKJ;djwebapp2ep8(*&2afaf'


class Utils():
    def blog_key(self, name='default'):
        return db.Key.from_path('post', name)

    def hash_str(self, s):
        return hmac.new(SECRET, s).hexdigest()

    def make_secure_val(self, s):
        return "%s|%s" % (s, self.hash_str(s))

    def check_secure_val(self, h):
        val = h.split('|')[0]
        if h == self.make_secure_val(val):
            return val

    def make_secure_val2(self, n, o):
        j = self.make_pw_hash(n, o)
        value = j.split(',')[0]
        return "%s|%s" % (n, value)

    def render_str(self, template, **params):
        t = main.jinja_env.get_template(template)
        return t.render(params)

    def render_post(response, post):
        response.out.write('<b>' + post.subject + '</b><br>')
        response.out.write(post.content)

    def make_salt(self, length=5):
        return ''.join(random.choice(letters) for x in xrange(length))

    def make_pw_hash(self, name, pw, salt=None):
        if not salt:
            salt = self.make_salt()
        h = hashlib.sha256(name + pw + salt).hexdigest()
        return '%s, %s' % (salt, h)

    def valid_pw(self, name, password, h):
        salt = h.split(',')[0]
        return h == self.make_pw_hash(name, password, salt)

    def valid_username(self, username):
        USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
        return username and USER_RE.match(username)

    def valid_password(self, password):
        PASS_RE = re.compile(r"^.{3,20}$")
        return password and PASS_RE.match(password)

    def valid_email(self, email):
        EMAIL_RE = re.compile(r'^[\S]+@[\S]+\.[\S]+$')
        return not email or EMAIL_RE.match(email)

    def post_exists(function):
        @wraps(function)
        def wrapper(self, post_id):
            key = db.Key.from_path("Post", int(post_id),
                                   parent=self.blog_key())
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
        Decorator to confirm user is logged in, otherwise redirected
        """
        def login(self, *args, **kwargs):
            # Redirect to login if user is not logged in, else execute function
            if not self.user:
                self.redirect("/login")
            else:
                func(self, *args, **kwargs)
        return login
