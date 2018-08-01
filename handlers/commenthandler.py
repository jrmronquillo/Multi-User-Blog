from handlers.bloghandler import BlogHandler
from handlers.decorators import login_required, post_exists
from models.Comment import Comment


class commentHandler(BlogHandler):
    @login_required
    @post_exists
    def get(self, post_id, posts):
        self.render("comment.html", post_id=post_id, error="")

    @login_required
    @post_exists
    def post(self, post_id, posts):
        content = self.request.get('content')
        name = self.user.name
        # created = self.request.get('created')

        # key = db.Key.from_path('Post', int(post_id), parent=blog_key())
        # posts = db.get(key)
        # if posts is None:
        #    return self.redirect('/blog')
        if content:
            c = Comment(comment=content, name=name, post_id=posts,
                        postId=int(post_id))
            c.put()
            return self.redirect('/blog')
        else:
            error = "content is required"
            self.render('comment.html', content=content, error=error)
