from handlers.bloghandler import BlogHandler
from handlers.decorators import user_logged_in


class about(BlogHandler):
    # Renders simple static about page with text.
    @user_logged_in
    def get(self, user, error):
        self.render('about.html', username=user)
