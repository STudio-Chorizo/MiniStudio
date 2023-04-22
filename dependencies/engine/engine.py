from asyncio.windows_events import NULL
import moderngl
import pygame as pg
import dependencies.moderngl.main as loadgl
from dependencies.parsejson.parse import *
from dependencies.engine.engine import *
from dependencies.engine.gameobject import *
from dependencies.scripts.entities.player import *
import time
import pygame

class Engine:
    Instance = NULL
    @staticmethod
    def CreateInstance(wW = 1200, wH = 800):
        if(Engine.Instance != NULL) : return
        Engine.Instance = Engine(wW, wH)

    def __init__(self, wW = 1200, wH = 800):
        if(Engine.Instance != NULL) : return
        self.player = GameObject()
        self.wW = wW
        self.wH = wH

        self.gameObjects = {}
        self.objectsCount = 0

        pg.init()
        self.window = pg.display.set_mode((wW,wH))
        self.surface = pygame.Surface((self.wW, self.wH), flags=pygame.SRCALPHA)

        self.run = True
        self.event = NULL
        self.time = 0
        self.lastTime = 0
        self.deltaTime = 0.0
        self.infoplayer = Guiplayer()
        
        self.graphicEngine = loadgl.GraphicsEngine((wW, wH))
    
    def LoadScene(self, sceneName):
        i = 0
        j = len(SCENES[sceneName])
        for obj in SCENES[sceneName]:
            print("loaded: " + str(i) + "/" + str(j) + " | load object: \"" + obj["name"] + "\" of type: \"" + obj["type"] + "\"")
            i += 1
            match obj["type"]:
                case "Player":
                    player = Player(obj["name"], obj["pos"], obj["rot"], obj["scale"])
                    self.AddGameObject(player)
                case "GameObject":
                    gameObject = GameObject(obj["name"], obj["pos"], obj["rot"], obj["scale"])
                    self.AddGameObject(gameObject)
        print("Load complete")
    
    def AddGameObject(self, gameObject):
        gameObject.UID = self.objectsCount.__str__()
        self.gameObjects[gameObject.UID] = gameObject
        self.objectsCount += 1

    def Start(self):
        self.lastTime = pg.time.get_ticks()
        self.Update()

    def Update(self):
        while(self.run):
            self.time = pg.time.get_ticks()
            self.deltaTime = self.time - self.lastTime
            self.lastTime = pg.time.get_ticks()

            self.event = pg.event.get()
            for e in self.event:
                if (e.type == pg.QUIT or e.type == pg.KEYDOWN and e.key == pg.K_ESCAPE) : self.run = False

            for obj in self.gameObjects:
                self.gameObjects[obj].Update()

            self.graphicEngine.get_time()
            self.graphicEngine.check_events()
            self.graphicEngine.camera.update()
            self.infoplayer.LifePlayer()
            self.graphicEngine.render(self.surface)
            pygame.display.flip()
            self.graphicEngine.delta_time = self.graphicEngine.clock.tick(60)
            
class Guiplayer:
    def __init__(self):
        self.life = 3
        self.mun = 14
        
    def LifePlayer(self):        
        pygame.draw.rect(Engine.Instance.surface, (0, 255, 0), pygame.rect.Rect(0, 0, 50, 50))
        
        