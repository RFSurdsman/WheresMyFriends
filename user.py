from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, username, password):
        self.id = id()
        self.username = username
        self.password = password
        self.friends = []
        self.position = (0, 0)

    def update_position(self, longitude, latitude):
        self.position = (longitude, latitude)

    def get_position(self):
        return self.position

    def add_friend(self, user):
        self.friends.append(user)

    def get_friends(self, user):
        return self.friends
