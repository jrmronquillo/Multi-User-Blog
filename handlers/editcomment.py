from handlers.bloghandler import BlogHandler
from handlers.decorators import (login_required, user_owns_comment,
                                 comment_exists)


class editComment(BlogHandler):
    @login_required
    @comment_exists
    @user_owns_comment
    def get(self, comment_id, comment):
        self.render("edit_comment.html", comment=comment)

    @login_required
    @comment_exists
    @user_owns_comment
    def post(self, comment_id, comment):
        print "edit comment post requested!"
        self.render("edit_comment.html", comment=comment)
        content = self.request.get('content')
        if content:
            comment.comment = content
            comment.put()
            return self.redirect('/blog/?')
        else:
            error = "Comment content required!"
            self.render('edit_comment.html', comment=comment,
                        error=error)
