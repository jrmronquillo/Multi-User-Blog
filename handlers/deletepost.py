from handlers.bloghandler import BlogHandler
from handlers.decorators import login_required, post_exists, user_owns_post


class deletePost(BlogHandler):
    @login_required
    @post_exists
    @user_owns_post
    def get(self, post_id, post):
        # key = db.Key.from_path('Post', int(post_id), parent=blog_key())
        # post = db.get(key)
        # if (self.user.name == post.author.name):
        self.render('deletepost.html', post_id=id)
        # else:
        #       error = "Only author can delete post"
        #       self.redirect('/blog')

    @login_required
    @post_exists
    @user_owns_post
    def post(self, post_id, post):
        # key = db.Key.from_path('Post', int(post_id), parent=blog_key())
        # post = db.get(key)
        post.delete()
        self.redirect('/blog')
