from handlers.bloghandler import BlogHandler
# from utils import Utils
from handlers.decorators import login_required, post_exists


class PostPage(BlogHandler):
    @login_required
    @post_exists
    def get(self, post_id, post):
        self.render("permalink.html", post=post, user=self.user.name)
