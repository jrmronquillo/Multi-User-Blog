from handlers.bloghandler import BlogHandler
from handlers.decorators import login_required
from models.Post import Post
from handlers.utils import Utils


class NewPost(BlogHandler):
    @login_required
    def get(self):
        self.render('newpost.html', username=self.user.name)

    @login_required
    def post(self):
        subject = self.request.get('subject')
        content = self.request.get('content')

        if subject and content:
            p = Post(parent=Utils().blog_key(), author=self.user,
                     subject=subject, content=content)
            p.put()
            return self.redirect('/blog/%s' % str(p.key().id()))
        else:
            error = "subject and content are both needed!"
            self.render("newpost.html", subject=subject,
                        content=content, error=error)
