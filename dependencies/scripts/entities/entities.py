
from dependencies.engine.gameobject import *
import dependencies.scripts.entities.ennemie as enm
import dependencies.engine.engine as eng
import pygame as pg

class Entities(GameObject):
    def __init__(self, reloadTime = 1, pos=..., rot=..., scale=...):
        super().__init__(pos, rot, scale)
        self.speed = 0.01
        self.rotSpeed = 0.3
        self.life = 1
        self.atkDistance = 100
        self.atk = 1
        self.reload = reloadTime
        self.lastAtk = 0

    def OnCollide(self, colider):
        self.Dmg(1)
    
    def Update(self):
        if self.life == 0:
            self.Die()
        return super().Update()
    
    def Atk(self):
        if(self.lastAtk + self.reload > eng.Engine.Instance.time) : return
        hit = self.Raycast(eng.FORWARD, self.atkDistance)
        if(hit == False or Entities.IsEntities(hit[0]) == False) : return
        hit[0].Dmg(self.atk)
        self.lastAtk = eng.Engine.Instance.time
        
    def Dmg(self, dmg):
        self.life -= dmg
        print("pv: " + self.life.__str__())
        if(self.life <= 0) : self.Die()
    
    def Die(self):
        self.Destroy()

    @staticmethod
    def IsEntities(obj):
        return type(obj) == enm.Ennemie or type(obj) == Player
    


class Player(Entities):
    def __init__(self, reloadTime = 1, pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1)):
        self.vue = 0
        self.lastTimeVueSwitch = 0
        self.speed = 0.01
        self.rotSpeed = 0.1
        self.scrollSpeed = 0.03
        super().__init__(reloadTime, pos, rot, scale)
        self.cameraOffset = glm.vec3([0, 0.2, -0.5])
        self.SetRotCamera((-10, 90, 0))

        self.life = 3
        self.Maxlife = self.life
        self.mun = 20
        self.guiplayer = eng.Guiplayer()

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

    def Update(self):
        if self.life == 0: return
        keys = pg.key.get_pressed()
        rotX = 0
        rotY = 0
        rotZ = 0
        if keys[pg.K_SPACE]:
            self.Atk()
        #Position
        if keys[pg.K_z]:
            self.Move(eng.UP * self.speed * eng.Engine.Instance.deltaTime)
            rotX = 1
        if keys[pg.K_s]:
            self.Move(-eng.UP * self.speed * eng.Engine.Instance.deltaTime)
            rotX = -1
        if keys[pg.K_d]:
            self.Move(-eng.RIGHT * self.speed * eng.Engine.Instance.deltaTime)
            rotZ = 1
        if keys[pg.K_q]:
            self.Move(eng.RIGHT * self.speed * eng.Engine.Instance.deltaTime)
            rotZ = -1
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
        #Cheat code start
        if keys[pg.K_a]:
            self.position = glm.vec3([0, 0, 0])
            self.rotation = glm.vec3([0, 0, 0])
        else:
        #Cheat code end
            self.Move(eng.FORWARD * self.scrollSpeed * eng.Engine.Instance.deltaTime)
            
            maxAngle = 25
            if(self.rotation[0] > maxAngle or self.rotation[0] < -maxAngle) : rotX = 0
            if(self.rotation[2] > maxAngle or self.rotation[2] < -maxAngle) : rotZ = 0
            
            if(rotX == 0 and (keys[pg.K_z] or keys[pg.K_s]) == False):
                if(self.rotation[0] > 0.2) : rotX = -1
                elif(self.rotation[0] < -0.2) : rotX = 1
            if(rotZ == 0 and (keys[pg.K_q] or keys[pg.K_d]) == False):
                if(self.rotation[2] > 0.2) : rotZ = -1
                elif(self.rotation[2] < -0.2) : rotZ = 1

            self.Rotate(self.rotSpeed * eng.Engine.Instance.deltaTime, glm.vec3([rotX, rotY, rotZ]))

        eng.Engine.Instance.graphicEngine.camera.position = self.position + self.cameraOffset
        if(self.vue == 1) : self.SetRotCamera((0, 90, 0))
        self.guiplayer.LifePlayer(self.life,self.mun,self.Maxlife)

        super().Update()