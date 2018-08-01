# !/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import os

import jinja2
import webapp2

from handlers.about import about
from handlers.blogfront import BlogFront
from handlers.commenthandler import commentHandler
from handlers.deletecomment import deleteComment
from handlers.deletepost import deletePost
from handlers.editcomment import editComment
from handlers.editpost import editPost
from handlers.likepost import LikePost
from handlers.login import Login
from handlers.logout import Logout
from handlers.mainpage import MainPage
from handlers.newpost import NewPost
from handlers.postpage import PostPage
from handlers.register import Register
from handlers.welcome import Welcome
from handlers.unit3welcome import Unit3Welcome
from handlers.unit2signup import Unit2Signup


template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir),
                               autoescape=True)

app = webapp2.WSGIApplication([
                               ('/', MainPage),
                               ('/unit2/signup', Unit2Signup),
                               ('/unit2/welcome', Welcome),
                               ('/signup', Register),
                               ('/login', Login),
                               ('/blog/?', BlogFront),
                               ('/about', about),
                               ('/blog/([0-9]+)', PostPage),
                               ('/blog/([0-9]+)/like', LikePost),
                               ('/blog/([0-9]+)/edit', editPost),
                               ('/blog/([0-9]+)/delete', deletePost),
                               ('/blog/([0-9]+)/comment', commentHandler),
                               ('/blog/([0-9]+)/editComment', editComment),
                               ('/blog/([0-9]+)/deleteComment', deleteComment),
                               ('/newPost', NewPost),
                               ('/logout', Logout),
                               ('/unit3/welcome', Unit3Welcome),
                               ], debug=True)
