import moderngl
import pygame as pg
from dependencies.engine.Untils.pool import Pool
import dependencies.moderngl.main as loadgl
from dependencies.parsejson.parse import *
from dependencies.engine.engine import *
from dependencies.engine.gameobject import *
from dependencies.scripts.entities.ennemie import Ennemie
from dependencies.music.music_control import Playlist
from dependencies.scripts.entities.entities import Player
from dependencies.scripts.gui.menu import Menu
import numpy
import time

from dependencies.scripts.spawn import Spawn


RIGHT = glm.vec3(1, 0, 0)
UP = glm.vec3(0, 1, 0)
FORWARD = glm.vec3(0, 0, 1)

class Engine:
    Instance = None
    @staticmethod
    def CreateInstance(wW = 1920, wH = 1080, Lang = "fr"):
        if(Engine.Instance != None) : return
        Engine.Instance = Engine(wW, wH, Lang)

    def __init__(self, wW = 1920, wH = 1080, Lang = "fr"):
        if(Engine.Instance != None) : return
        self.player = GameObject()
        self.wW = wW
        self.wH = wH

        self.gameObjects = {}
        self.objectsCount = 0

        self.allLangs = ["fr","en"]
        self.selectLang = 0

        pg.init()
        self.window = pg.display.set_mode((wW,wH))
        self.surface = pg.Surface((self.wW, self.wH), flags=pg.SRCALPHA)

        self.run = True
        self.event = None
        self.time = 0
        self.lastTime = 0
        self.deltaTime = 0.0
        self.speedTime = 0
        
        self.pool = {}
        
        self.graphicEngine = loadgl.GraphicsEngine((wW, wH))

        self.MasterVolume = Playlist.Instance.masterVolume

        self.lang = Lang
        self.Dialog = loadDialog(self.lang)
        self.menu = Menu(self)
    
    def LoadScene(self, sceneName):
        i = 0
        j = len(SCENES[sceneName])
        for obj in SCENES[sceneName]:
            if(obj["nb"] != 1) : self.pool[obj["name"]] = Pool()
            for k in range(obj["nb"]) :
                print("loaded: " + str(i) + "/" + str(j) + " | load object: \"" + obj["name"] + "\" of type: \"" + obj["type"] + "\"")
                i += 1
                gameObject = None
                match obj["type"]:
                    case "Player":
                        gameObject = Player(1, obj["pos"], obj["rot"], obj["scale"])
                        self.player = gameObject
                    case "GameObject":
                        gameObject = GameObject(obj["pos"], obj["rot"], obj["scale"])
                    case "Spawn":
                        gameObject = Spawn(obj["name"], 10, obj["pos"], obj["rot"], obj["scale"])
                    case "Ennemie":
                        gameObject = Ennemie(2, obj["pos"], obj["rot"], obj["scale"])
                
                print(gameObject.forward)
                if(gameObject == None) : continue
                if(obj["obj"] != None) : gameObject.SetModel(obj["obj"])
                if(obj["collider"] != None) : gameObject.SetCollider(obj["collider"])
                self.AddGameObject(gameObject)
                if(obj["nb"] != 1):
                    self.pool[obj["name"]].Add(gameObject)
        
        print("Load complete")
    
    def AddGameObject(self, gameObject):
        gameObject.UID = self.objectsCount.__str__()

        print(gameObject.UID)
        self.gameObjects[gameObject.UID] = gameObject
        self.objectsCount += 1

    def Destroy(self, UID):
        self.gameObjects[UID].Destroy()
        del self.gameObjects[UID]
    
    def IsCollide(self, col1, col2):
        if(col1.UID == col2.UID) : return False
        pos1 = col1.velocity + col1.collideBox + (col1.position[0], col1.position[1], col1.position[2])
        posn1 = col1.velocity - col1.collideBox + (col1.position[0], col1.position[1], col1.position[2])
        axisIn = 0
        for i in range(3):
            pos2 = col2.position[i] + col2.collideBox[i]
            posn2 = col2.position[i] - col2.collideBox[i]
            if(pos1[i] > posn2 and pos1[i] < pos2 or posn1[i] > posn2 and posn1[i] < pos2 or
               pos2 > posn1[i] and pos2 < pos1[i] or posn2 > posn1[i] and posn2 < pos1[i] ) : axisIn += 1
        if(axisIn < 3) : return False
        return True

    def TestCollider(self, obj):
        if(obj.isCollide == False or obj.velocity == (0, 0, 0)) : return False
        for col in self.gameObjects:
            if(self.gameObjects[col].isCollide == False or self.IsCollide(obj, self.gameObjects[col]) == False) : 
                continue
            obj.Move(-3 * obj.velocity)
            obj.OnCollide(self.gameObjects[col])

            self.gameObjects[col].OnCollide(obj)
            break
        obj.velocity = (0, 0, 0)

    def Start(self):
        self.lastTime = pg.time.get_ticks()
        while(self.run):
            self.Update()

    def Update(self):
        self.time = pg.time.get_ticks()
        self.deltaTime = (self.time - self.lastTime) * self.speedTime
        self.lastTime = pg.time.get_ticks()

        self.event = pg.event.get()
        for e in self.event:
            if (e.type == pg.QUIT) : self.run = False
        
        self.surface.fill((0, 0, 0, 0))

        for obj in self.gameObjects:
            if(self.gameObjects[obj].isActive == True) : self.gameObjects[obj].Update()
            
        for o in self.gameObjects:
            if(self.gameObjects[o].isCollide == True) : self.TestCollider(self.gameObjects[o])

        self.graphicEngine.get_time()
        self.graphicEngine.check_events()
        self.graphicEngine.camera.update()
        self.menu.Update()
        self.graphicEngine.render(self.surface)
        Playlist.Instance.update()
        pg.display.flip()
        self.graphicEngine.delta_time = self.graphicEngine.clock.tick(60)