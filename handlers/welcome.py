from handlers.bloghandler import BlogHandler
from handlers.utils import Utils


class Welcome(BlogHandler):
    def get(self):
        cookieVal = self.request.cookies.get('name')
        username = cookieVal.split('|')[0]
        if Utils().valid_username(username):
            self.render("welcome.html", username=username)
        else:
            self.redirect('/signup')
