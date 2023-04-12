import time
import pygame as pg
import sys

class Engine:
    def __init__(self, wW, wH):
        self.wW = wW
        self.wH = wH

        self.gameObjects = {}
        self.objectsCount = 0
        pg.init()
        self.window = pg.display.set_mode((wW,wH))
        self.window.fill("black")

    def AddGameObject(self, obj):
        obj.UID = self.objectsCount.__str__()
        self.gameObjects[obj.UID] = obj
        self.objectsCount += 1
    
    def Update(self):
        for obj in self.gameObjects:
            self.gameObjects[obj].Update(self)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

        pg.display.update()
        time.sleep(0.1)
        self.Update()

