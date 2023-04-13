from asyncio.windows_events import NULL
import pygame as pg
import dependencies.moderngl.main as loadgl

class Engine:
    Instance = NULL
    @staticmethod
    def CreateInstance(wW = 1200, wH = 800):
        if(Engine.Instance != NULL) : return
        Engine.Instance = Engine(wW, wH)

    def __init__(self, wW = 1200, wH = 800):
        if(Engine.Instance != NULL) : return
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

        
        self.graphicEngine = loadgl.GraphicsEngine((wW, wH))
    
    def AddGameObject(self, gameObject):
        gameObject.UID = self.objectCount.__str__()
        self.gameObject[gameObject.UID] = gameObject
        self.objectsCount += 1
    
    def Start(self):
        self.lastTime = pg.time.get_ticks()
        self.Update()

    def Update(self):
        while(self.run):
            self.time = pg.time.get_ticks()
            self.deltaTime = self.time - self.lastTime

            self.event = pg.event.get()
            for e in self.event:
                if e.type == pg.QUIT : self.run = False

            for obj in self.gameObjects:
                self.gameObjects[obj].Update()

            self.graphicEngine.get_time()
            self.graphicEngine.check_events()
            self.graphicEngine.camera.update()
            self.graphicEngine.render()
            self.graphicEngine.delta_time = self.graphicEngine.clock.tick(60)
            
            self.lastTime = pg.time.get_ticks()

