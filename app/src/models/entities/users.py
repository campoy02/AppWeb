from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, id, username, password, usertype, fullname="", email="") -> None:
        self.id = id
        self.username = username
        self.password = password
        self.fullname = fullname
        self.email = email
        self.usertype = usertype
