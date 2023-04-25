from random import *
from dependencies.engine.gameobject import *
import dependencies.scripts.entities.ennemie as enm
import dependencies.engine.engine as eng
import pygame as pg
from dependencies.parsejson.parse import *

class Entities(GameObject):
    def __init__(self, reloadTime = 1, pos=..., rot=..., scale=...):
        super().__init__(pos, rot, scale)
        self.speed = 0.01
        self.rotSpeed = 0.3
        self.life = 1
        self.atkDistance = 100
        self.atk = 1
        self.reload = reloadTime * 1000
        self.lastAtk = 0

    def OnCollide(self, colider):
        self.Dmg(1)
    
    def Update(self):
        if self.life == 0:
            self.Die()
        return super().Update()
    
    def Atk(self):
        if(self.lastAtk + self.reload > eng.Engine.Instance.time) : return
        self.UpdateLocalAxis()
        hit = self.Raycast(eng.FORWARD * self.forward, self.atkDistance)
        if(hit == False or Entities.IsEntities(hit[0]) == False) : return
        hit[0].Dmg(self.atk)
        self.lastAtk = eng.Engine.Instance.time
        
    def Dmg(self, dmg):
        self.life -= dmg
        print(self.UID + "pv: " + self.life.__str__())
        if(self.life <= 0) : self.Die()
    
    def Die(self):
        self.Destroy()

    @staticmethod
    def IsEntities(obj):
        return type(obj) == enm.Ennemie or type(obj) == Player
    


class Player(Entities):
    def __init__(self, reloadTime = 1, pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1)):
        self.vue = 0
        self.cheatLifeUp = 0
        self.cheatLifeDown = 0
        self.lastTimeVueSwitch = 0
        self.speed = 0.01
        self.rotSpeed = 0.1
        self.scrollSpeed = 0.03
        self.breakWing = choice([-1,1])
        rot[1] -= 180
        super().__init__(reloadTime, pos, rot, scale)
        self.cameraOffset = glm.vec3([0, 0.15, -0.26])
        self.SetRotCamera((-10, 90, 0))

        self.life = 3
        self.Maxlife = self.life
        self.mun = 20

    def SetRotCamera(self, camOrientation: tuple = (0, 0, 0), local = True) -> None:
        cam = eng.Engine.Instance.graphicEngine.camera
        rot = camOrientation
        if(local == True) : rot += glm.radians(self.rotation)
        cam.pitch = rot[0]
        cam.yaw = rot[1]
        cam.roll = rot[2]
    
    def Die(self):
        # dernière mise à jour de la GUI
        self.life = math.exp(-16)
        self.Update()
        self.life = 0

        # Annonce de la mort du joueur
        print("Vous êtes mort")
    
    
    def drawLifePlayer(self):
        sizeBar = int(eng.Engine.Instance.wW * 0.3)

        RespwH = int(eng.Engine.Instance.wH *0.8875)
        RespwW = int(eng.Engine.Instance.wW *0.025)
        
        RespSize = int((sizeBar / self.Maxlife) * self.Maxlife)
        RespLife = int(RespSize -((self.Maxlife-self.life)*(sizeBar/self.Maxlife)))
        RespHeight = int(eng.Engine.Instance.wW * 0.05)

        background = pg.Rect(RespwW, RespwH, RespSize, RespHeight)
        lifebar = pg.Rect(RespwW, RespwH, RespLife, RespHeight)

        pg.draw.rect(eng.Engine.Instance.surface, (100, 100, 100), background)
        pg.draw.rect(eng.Engine.Instance.surface, (0, 255, 0), lifebar)

    def Update(self):
        if self.life == 0: return
        keys = pg.key.get_pressed()
        rotX = 0
        rotY = 0
        rotZ = 0
        #Influence de la vie sur le gamplay
        if (self.life <= int(self.Maxlife * 2 / 3)):
            problems = random() *1.2
            self.Move(eng.RIGHT * self.speed * eng.Engine.Instance.deltaTime * self.breakWing * problems)
            rotZ -= problems * self.breakWing

            if (self.life <= int(self.Maxlife / 3)):
                nausea = pg.image.load(ASSETS["nausea"]["dir"]).convert_alpha()
                nausea = pg.transform.scale(nausea, (eng.Engine.Instance.wW, eng.Engine.Instance.wH))
                eng.Engine.Instance.surface.blit(nausea, (0, 0))
        #Attaque
        if keys[pg.K_SPACE]:
            self.Atk()
        #Position
        if keys[pg.K_z]:
            self.Move(eng.UP * self.speed * eng.Engine.Instance.deltaTime)
            rotX += 1
        if keys[pg.K_s]:
            self.Move(-eng.UP * self.speed * eng.Engine.Instance.deltaTime)
            rotX += -1
        if keys[pg.K_d]:
            self.Move(-eng.RIGHT * self.speed * eng.Engine.Instance.deltaTime)
            rotZ += 1
        if keys[pg.K_q]:
            self.Move(eng.RIGHT * self.speed * eng.Engine.Instance.deltaTime)
            rotZ += -1
        #Caméra
        if(keys[pg.K_e] and self.lastTimeVueSwitch + 300 < eng.Engine.Instance.time):
            self.lastTimeVueSwitch = eng.Engine.Instance.time
            #1er personne
            if (self.vue == 0):
                self.cameraOffset = glm.vec3([0, 0, 0])
                self.vue = 1
            #3ème personne
            elif (self.vue == 1):
                self.cameraOffset = glm.vec3([0, 0.2, -0.5])
                self.SetRotCamera((-10, 90,0), False)
                self.vue = 0
        #Cheat code life
        if keys[pg.K_p] and self.cheatLifeUp == 0:
            self.life += 1
            self.cheatLifeUp = 1
        elif keys[pg.K_p] == False and self.cheatLifeUp == 1:
            self.cheatLifeUp = 0
        if keys[pg.K_m] and self.cheatLifeDown == 0:
            self.life -= 1
            self.cheatLifeDown = 1
        elif keys[pg.K_m] == False and self.cheatLifeDown == 1:
            self.cheatLifeDown = 0
        #Cheat code start
        if keys[pg.K_a]:
            self.position = glm.vec3([0, 0, 0])
            self.rotation = glm.vec3([0, -180, 0])
        else:
        #Cheat code end
            self.Move(eng.FORWARD * self.scrollSpeed * eng.Engine.Instance.deltaTime)
            
            maxAngle = 25
            if(self.rotation[0] > maxAngle or self.rotation[0] < -maxAngle) : rotX = 0
            if(self.rotation[2] > maxAngle or self.rotation[2] < -maxAngle) : rotZ = 0
            
            if(rotX == 0):
                if(self.rotation[0] > 3 and keys[pg.K_z] == False) : rotX += -1
                elif(self.rotation[0] < -3 and keys[pg.K_s] == False) : rotX += 1
            if(rotZ == 0):
                if(self.rotation[2] > 3 and keys[pg.K_d] == False) : rotZ += -1
                elif(self.rotation[2] < -3 and keys[pg.K_q] == False) : rotZ += 1

            self.Rotate(self.rotSpeed * eng.Engine.Instance.deltaTime, glm.vec3([rotX, rotY, rotZ]))

        eng.Engine.Instance.graphicEngine.camera.position = self.position + self.cameraOffset
        if(self.vue == 1) : self.SetRotCamera((0, 90, 0))
        self.drawLifePlayer()

        super().Update()