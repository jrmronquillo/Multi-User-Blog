from handlers.bloghandler import BlogHandler


class Logout(BlogHandler):
    def get(self):
        if self:
            self.logout()
            return self.redirect('/signup')
        else:
            self.redirect('/signup')
