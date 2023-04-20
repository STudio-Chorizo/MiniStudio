from asyncio.windows_events import NULL
import pygame as pg

class Engine:
    def __init__(self, wW, wH):
        self.wW = wW
        self.wH = wH

        self.gameObjects = {}
        self.objectsCount = 0
        pg.init()
        self.window = pg.display.set_mode((wW,wH))
        self.run = True
        self.event = NULL
        self.time = 0
        self.lastTime = 0
        self.deltaTime = 0

    def AddGameObject(self, gameObject):
        gameObject.UID = self.objectCount.__str__()
        self.gameObject[gameObject.UID] = gameObject
        self.objectsCount += 1
    
    def Start(self):
        self.lastTime = pg.time.get_ticks()
        self.Update()

    def Update(self):
        self.time = pg.time.get_ticks()
        self.deltaTime = self.time - self.lastTime

        for obj in self.gameObjects:
            if(obj.isActive) : self.gameObjects[obj].Update()
        
        self.event = pg.event.get()
        for e in self.event:
            if e.type == pg.QUIT : self.run = False
            
        self.lastTime = pg.time.get_ticks()
        if(self.run) : self.Update()

