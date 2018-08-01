from handlers.bloghandler import BlogHandler
from google.appengine.ext import db
from handlers.decorators import user_logged_in


class BlogFront(BlogHandler):
    @user_logged_in
    def get(self, user, error=""):
        posts = db.GqlQuery("select * from Post order by created "
                            "desc limit 10")
        self.render('blogfront.html', posts=posts, user=user, error=error)

        # comments = db.GqlQuery("select * from Comment")
        # self.render('blogfront.html', posts=posts, comments=comments,
        #            user=user, error=error)
        # if self.user:
        #    self.render('blogfront.html', posts=posts, comments=comments,
        #                user=user, error=error)
        # else:
        #    self.render('blogfront.html', posts=posts, comments=comments,
        #                user=user, error=error)
    @user_logged_in
    def post(self):
        posts = db.GqlQuery("select * from Post order by"
                            "created desc limit 10")
        self. render('blogfront.html', posts=posts)
        # comments = db.GqlQuery("select * from Comment")

        # if self.user:
        #    self.render('blogfront.html', posts=posts, comments=comments,
        #                user=self.user.name, error="")
        # else:
        #    self.render('blogfront.html', posts=posts, comments=comments,
        #                user='Guest', error="User not Defined")

        # self.render('blogfront.html', posts=posts, comments=comments)
