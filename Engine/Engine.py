import pygame as pg

class Engine:
    def __init__(self, wW, wH):
        self.wW = wW
        self.wH = wH

        self.gameObjects = {}
        self.objectsCount = 0
        pg.init()
        self.window = pg.display.set_mode((wW,wH))

    def AddGameObject(self, gameObject):
        gameObject.UID = self.objectCount.__str__()
        self.gameObject[gameObject.UID] = gameObject
        self.objectsCount += 1
    
    def Update(self):
        for obj in self.gameObjects:
            self.gameObjects[obj].Update(self)
        self.Update()

