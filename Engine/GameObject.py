

class GameObject:
    def __init__(self, position = [0, 0, 0], rot = [0, 0, 0], scale = [0, 0, 0]):
        self.position = position
        self.rotation = rot
        self.scale = scale
        self.UID = "-1"

    def Update(self, engine):
        pass