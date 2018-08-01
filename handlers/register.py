from handlers.signup import signup
from models.user import User


class Register(signup):
    def done(self):
        # check that user doesnt already exist
        u = User.by_name(self.username)
        if u:
            msg = 'That user already exists.'
            self.render('sign_up.html', error_username=msg)
        else:
            u = User.register(self.username, self.password, self.email)
            u.put()
            self.login(u)
            self.redirect('/unit3/welcome')
