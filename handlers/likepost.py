from handlers.bloghandler import BlogHandler
from handlers.decorators import login_required, post_exists, user_owns_post
from models.likes import Likes


class LikePost(BlogHandler):
    @login_required
    @post_exists
    def post(self, post_id, posts):
        name = self.user.name

        if name == posts.author.name:
            print 'user attempting to like own post'
            return self.redirect("/blog/?")

        if self.user.name in posts.LikersArray:
            print "user found like user_like array"
            return self.redirect('/blog')
        else:
            print "user not in posts array"
            posts.LikersArray.append(self.user.name)
            # posts.like_count += 1
            # print posts.LikersArray
            # print posts.like_count
            print posts.likes
            posts.put()
            l = Likes(name=self.user.name, post_id=int(post_id))
            l.put()
            return self.redirect('/blog')
