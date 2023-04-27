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
from dependencies.scripts.entities.bullets import Bullet
from dependencies.scripts.gui.menu import Menu
import dependencies.scripts.utilitaries.joystick as js
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
        self.wW = wW
        self.wH = wH
        self.guiPlayer = Guiplayer(wW, wH)
        self.player = GameObject("player")

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
        self.MasterVolume = {"master": 100, "music": 100, "vfx": 100}

        pg.joystick.init()
        self.numJoystick = 0
        self.joystick = js.MyJoysitck()
        self.joystick.init()
        self.JoystickInit()


    def JoystickInit(self):
        if pg.joystick.get_count() > self.numJoystick :
            print("new joystick detected, the active joystick is: " + pg.joystick.Joystick(0).get_name())
        elif pg.joystick.get_count() < self.numJoystick :
            print("joystick disconnected")
        else: return

        self.numJoystick = pg.joystick.get_count()
        self.joystick = js.MyJoysitck()
        self.joystick.init()
    
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
                        gameObject = Player(obj["name"], 1, obj["pos"], obj["rot"], obj["scale"])
                        self.player = gameObject
                    case "GameObject":
                        gameObject = GameObject(obj["name"], obj["pos"], obj["rot"], obj["scale"])
                    case "Spawn":
                        gameObject = Spawn(obj["name"], 10, obj["pos"], obj["rot"], obj["scale"])
                    case "Ennemie":
                        gameObject = Ennemie(obj["name"], 2, obj["pos"], obj["rot"], obj["scale"])
                    case "Bullet":
                        gameObject = Bullet(obj["name"], obj["pos"], obj["rot"], obj["scale"])
                
                if(gameObject == None) : continue
                if(obj["obj"] != None) : gameObject.SetModel(obj["obj"])
                if(obj["collider"] != None) : gameObject.SetCollider(obj["collider"])
                self.AddGameObject(gameObject)
                if(obj["nb"] != 1):
                    self.pool[obj["name"]].Add(gameObject)
        
        print("Load complete")
    
    def AddGameObject(self, gameObject):
        gameObject.UID = self.objectsCount.__str__()
        self.gameObjects[gameObject.UID] = gameObject
        self.objectsCount += 1

    def Destroy(self, UID):
        if(UID in self.gameObjects and self.gameObjects[UID].Destroy() == True):
            self.gameObjects[UID].position = glm.vec3(0, 0, -100)
            self.gameObjects[UID].Update()
            self.gameObjects[UID].isActive = False
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
            obj.OnCollide(self.gameObjects[col])
            self.gameObjects[col].OnCollide(obj)
            break

    def Start(self):
        self.lastTime = pg.time.get_ticks()
        while(self.run):
            self.Update()

    def Update(self):

        self.JoystickInit()

        self.time = pg.time.get_ticks()
        self.deltaTime = (self.time - self.lastTime) * self.speedTime
        self.lastTime = pg.time.get_ticks()

        self.event = pg.event.get()
        
        for e in self.event:
            if (e.type == pg.QUIT) : self.run = False
        
        self.surface.fill((0, 0, 0, 0))

        object = dict(self.gameObjects)
        for obj in object:
            if(object[obj].isActive == True) : object[obj].Update()
            
        for o in object:
            if(object[o].isActive == True and object[o].isCollide == True) : self.TestCollider(object[o])
        self.gameObjects = object

        self.graphicEngine.get_time()
        self.graphicEngine.check_events()
        self.graphicEngine.camera.update()
        self.menu.Update()
        self.graphicEngine.render(self.surface)
        Playlist.Instance.update()
        pg.display.flip()
        self.graphicEngine.delta_time = self.graphicEngine.clock.tick(60)
            
class Guiplayer():
    def __init__(self, wW, wH):
        self.wW = wW
        self.wH = wH
        self.life = -1
        self.mun = -1
        self.maxlife = -1
        self.sizeBar = 0.51*self.wW
        self.RespwHmun = -1
        self.RespwHmunpos = -1
        self.RespwHlifebar = -1
        self.RespwWlifebar = -1
        self.RespSizelife = -1
        self.RespwHSizelife = -1
    def LifePlayer(self,life = -2,mun = -2,maxlife = -2):
        self.life = life
        self.mun = mun
        self.RespwHlifebar = Engine.Instance.wH*(6.71/9)
        self.RespwWlifebar = Engine.Instance.wW*(0.67/16)
        self.RespwHgg = Engine.Instance.wH *(7.95/9)
        self.RespwWgg = Engine.Instance.wW *(2.95/16)
        self.RespwWmun = Engine.Instance.wW *(1/160)
        self.RespwHmun = Engine.Instance.wH *(222.5/900)
        self.RespwHSizelife = self.wH*0.212
        self.maxlife = maxlife
        self.RespwHmunpos = self.RespwHlifebar + self.RespwHlifebar*0.025
        self.RespSizelife = int((Engine.Instance.wW*0.352 / self.maxlife) * self.maxlife) 
        self.RespLife = int(self.RespSizelife -((self.maxlife-self.life)*(Engine.Instance.wW*0.352/self.maxlife)))
        ScreenBorder = pg.image.load(ASSETS["guiplayer"]["ScreenBorder"]).convert_alpha()
        ScreenBorder = pg.transform.scale(ScreenBorder, (self.wW, self.wH))
        Engine.Instance.surface.blit(ScreenBorder, (0, 0))

        AimUiLightBlueWhite = pg.image.load(ASSETS["guiplayer"]["AimUiLightBlueWhite"]).convert_alpha()
        AimUiLightBlueWhite = pg.transform.scale(AimUiLightBlueWhite, (Engine.Instance.wW*0.062, Engine.Instance.wH*0.111))
        Engine.Instance.surface.blit(AimUiLightBlueWhite, (Engine.Instance.wW*0.5-((Engine.Instance.wW*0.062)/2), Engine.Instance.wH*0.5-((Engine.Instance.wH*0.111)/2)))
        EnergyBarre = pg.image.load(ASSETS["magazine"][str(self.mun)]).convert_alpha()
        EnergyBarre = pg.transform.scale(EnergyBarre, (Engine.Instance.wW*0.09, Engine.Instance.wH*0.451))
        Engine.Instance.surface.blit(EnergyBarre, (self.RespwWmun, self.RespwHmun))

        HealthBarCounters = pg.image.load(ASSETS["guiplayer"]["HealthBarCounters"]).convert_alpha()
        HealthBarCounters = pg.transform.scale(HealthBarCounters, (Engine.Instance.wW*0.495, Engine.Instance.wH*0.234))
        Engine.Instance.surface.blit(HealthBarCounters, (self.RespwWlifebar, self.RespwHlifebar))
        DroneHealthBarNegative = pg.image.load(ASSETS["guiplayer"]["DroneHealthBarNegative"]).convert_alpha()
        DroneHealthBarNegative = pg.transform.scale(DroneHealthBarNegative, (Engine.Instance.wW*0.352, Engine.Instance.wH*0.042))
        Engine.Instance.surface.blit(DroneHealthBarNegative, (self.RespwWgg,self.RespwHgg))
        DroneHealthBarPositive = pg.image.load(ASSETS["guiplayer"]["DroneHealthBarPositive"]).convert_alpha()
        DroneHealthBarPositive = pg.transform.scale(DroneHealthBarPositive, (abs(self.RespLife), Engine.Instance.wH*0.042))
        Engine.Instance.surface.blit(DroneHealthBarPositive, (self.RespwWgg,self.RespwHgg))
