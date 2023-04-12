

class GameObject:
    def __init__(self, pos = [0, 0, 0], rot = [0, 0, 0], scale = [0, 0, 0]):
        self.position = pos
        self.rotation = rot
        self.scale = scale
        self.UID = "-1"

    def Update(self, engine):
        pass

