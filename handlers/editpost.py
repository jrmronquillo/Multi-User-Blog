from handlers.bloghandler import BlogHandler
from handlers.decorators import login_required, post_exists, user_owns_post


class editPost(BlogHandler):
    @login_required
    @post_exists
    @user_owns_post
    def get(self, post_id, post):
        self.render('edit_post.html', post=post)

    @login_required
    @post_exists
    @user_owns_post
    def post(self, post_id, post):
        subject = self.request.get('subject')
        content = self.request.get('content')
        if subject and content:
            post.subject = subject
            post.content = content
            post.put()
            return self.redirect('/blog/%s' % str(post.key().id()))
        else:
            error = 'Both subject and content required, please retry edit!'
            return self.render("edit_post.html", post=post, error=error)
            print error
