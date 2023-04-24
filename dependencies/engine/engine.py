from asyncio.windows_events import NULL
import pygame as pg
import moderngl
import dependencies.moderngl.main as loadgl
from dependencies.parsejson.parse import *
from dependencies.engine.engine import *
from dependencies.engine.gameobject import *
from dependencies.scripts.entities.cat import Cat
from dependencies.scripts.entities.player import *
import numpy
import time


RIGHT = glm.vec3(1, 0, 0)
UP = glm.vec3(0, 1, 0)
FORWARD = glm.vec3(0, 0, -1)

class Engine:
    Instance = None
    @staticmethod
    def CreateInstance(wW = 1200, wH = 800):
        if(Engine.Instance != None) : return
        Engine.Instance = Engine(wW, wH)

    def __init__(self, wW = 1200, wH = 800):
        if(Engine.Instance != None) : return
        self.player = GameObject()
        self.wW = wW
        self.wH = wH

        self.gameObjects = {}
        self.objectsCount = 0
        pg.init()
        self.window = pg.display.set_mode((wW,wH))
        self.run = True
        self.event = None
        self.time = 0
        self.lastTime = 0
        self.deltaTime = 0.0

        
        self.graphicEngine = loadgl.GraphicsEngine((wW, wH))
    
    def LoadScene(self, sceneName):
        i = 0
        j = len(SCENES[sceneName])
        for obj in SCENES[sceneName]:
            print("loaded: " + str(i) + "/" + str(j) + " | load object: \"" + obj["name"] + "\" of type: \"" + obj["type"] + "\"")
            i += 1
            gameObject = None
            match obj["type"]:
                case "Player":
                    gameObject = Player((obj["pos"][0], obj["pos"][1], -obj["pos"][2]), obj["rot"], obj["scale"])
                case "GameObject":
                    gameObject = Cat((obj["pos"][0], obj["pos"][1], -obj["pos"][2]), obj["rot"], obj["scale"])
            
            if(gameObject == None) : continue
            if(obj["name"] != None) : gameObject.SetModel(obj["name"])
            if(obj["collider"] != None) : gameObject.SetCollider(obj["collider"])
            self.AddGameObject(gameObject)

        print("Load complete")
    
    def AddGameObject(self, gameObject):
        gameObject.UID = self.objectsCount.__str__()
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
                
            for o in self.gameObjects:
                if(self.gameObjects[o].isCollide == True) : self.TestCollider(self.gameObjects[o])

            self.graphicEngine.get_time()
            self.graphicEngine.check_events()
            self.graphicEngine.camera.update()
            self.graphicEngine.render()
            self.graphicEngine.delta_time = self.graphicEngine.clock.tick(60)

class Guiplayer():
    
    def __init__(self):
        self.life = -1
        self.mun = -1
        self.wW = 1200
        self.wH = 800

    def updateGui(self,life = -2,mun = -2):
        self.life = life
        self.mun = mun
        pg.draw.rect(Engine.Instance.s, (0, 255, 0), pg.rect.Rect(self.wW*0.025, self.wH*0.0625, self.life*100, 50))
            

