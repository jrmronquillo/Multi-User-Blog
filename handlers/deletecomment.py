from handlers.bloghandler import BlogHandler
from handlers.decorators import (login_required, comment_exists,
                                 user_owns_comment)


class deleteComment(BlogHandler):
    @login_required
    @comment_exists
    @user_owns_comment
    def get(self, comment_id, comment):
        self.render('deleteComment.html')

    @login_required
    @comment_exists
    @user_owns_comment
    def post(self, comment_id, comment):
        self.render("edit_comment.html", comment=comment)
        comment.delete()
        self.redirect('/blog')
