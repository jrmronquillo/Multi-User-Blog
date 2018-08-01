from handlers.signup import signup


class Unit2Signup(signup):
    def done(self):
        self.redirect('/unit2/welcome?username=' + self.username)
