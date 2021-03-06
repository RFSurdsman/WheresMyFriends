from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, username, password, filename, position, location):
        self.id = id(self)
        self.username = username
        self.password = password
        self.friends = []
        self.position = position
        self.imagelocation = filename + '.png'
        self.location = location

    def update_position(self, longitude, latitude):
        self.position = (longitude, latitude)

    def get_position(self):
        return self.position

    def add_friend(self, user):
        self.friends.append(user)

    def get_friends(self, user):
        return self.friends

    def get_ID(self):
        return self.id

    def get_map_pixels(self):
        xDiff = self.position[0] - 33.918216
        yDiff = self.position[1] - 151.231402

        return (450 + xDiff * 250000, 300 + yDiff * 4000)

    def get_pic(self):
        return self.imagelocation

