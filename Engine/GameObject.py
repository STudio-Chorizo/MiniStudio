from asyncio.windows_events import NULL


class GameObject:
    def __init__(self, pos = [0, 0, 0], rot = [0, 0, 0], scale = [0, 0, 0]):
        self.position = pos
        self.rotation = rot
        self.scale = scale
        self.UID = "-1"
        self.isCollide = False
        self.collideBox = NULL

    #Utiliser cette fonction pour avoir les collision
    def Move(self, translation):
        self.position += translation
        if(self.isCollide == False) : return
        #TO-DO test de colllision

    def Update(self, engine):
        pass

