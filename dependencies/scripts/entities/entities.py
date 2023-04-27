from random import *
from dependencies.engine.gameobject import *
from dependencies.scripts.entities.bullets import Bullet
import dependencies.scripts.entities.ennemie as enm
import dependencies.engine.engine as eng
import pygame as pg
from dependencies.parsejson.parse import *

class Entities(GameObject):
    def __init__(self, name, reloadTime = 1, pos=..., rot=..., scale=...):
        super().__init__(name, pos, rot, scale)
        self.speed = 0.01
        self.rotSpeed = 0.3
        self.life = 1
        self.Maxlife = self.life
        self.atkDistance = 100
        self.atk = 1
        self.reload = reloadTime * 1000
        self.lastAtk = 0

    def OnCollide(self, colider):
        if(type(colider) == Bullet) : return False
        self.Dmg(1)
        super().OnCollide(colider)
    
    def Update(self):
        return super().Update()
    
    def Atk(self):
        if(self.lastAtk + self.reload > eng.Engine.Instance.time) : return
        bullet = eng.Engine.Instance.pool["bullet"].Get()
        if(bullet == False) : return
        bullet.Shoot(self.UID, self.position, self.rotation)
        self.lastAtk = eng.Engine.Instance.time
        
    def Dmg(self, dmg):
        self.life -= dmg
        print("pv of entity " + self.name + " n°" + str(self.UID) + ": " + str(self.life) + "/" + str(self.Maxlife))
        if(self.life <= 0) : self.Die()
    
    def Die(self):
        self.Destroy()

    @staticmethod
    def IsEntities(obj):
        return type(obj) == enm.Ennemie or type(obj) == Player
    


class Player(Entities):
    def __init__(self, name, reloadTime = 1, pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1)):
        self.vue = 0
        self.cheatLifeUp = 0
        self.cheatLifeDown = 0
        self.lastTimeVueSwitch = 0
        self.rotSpeed = 0.1
        self.scrollSpeed = 0.01
        self.breakWing = choice([-1,1])
        super().__init__(name, reloadTime, pos, rot, scale)
        self.cameraOffset = glm.vec3([0, 0.15, -0.26])
        self.SetRotCamera((-10, 90, 0))

        self.life = 3
        self.Maxlife = self.life
        self.mun = 6
        self.guiPlayer = eng.Engine.Instance.guiPlayer
        self.modelRotation = glm.vec3([0, 180, 0])

        self.joystick = eng.Engine.Instance.joystick

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

    def OnCollide(self, colider):
        if(type(colider) == Bullet) : return False
        print("Touch by: " + colider.name)
        self.Dmg(1)

    def Update(self):
        if self.life == 0: return
        keys = pg.key.get_pressed()

        # print()
        rotX = -self.joystick.get_axis(1) if self.joystick.get_axis(1) > 0.1 or self.joystick.get_axis(1) < -0.1 else 0
        self.Move(eng.UP * self.speed * eng.Engine.Instance.deltaTime * rotX)
        rotY = 0
        rotZ = self.joystick.get_axis(0) if self.joystick.get_axis(0) > 0.1 or self.joystick.get_axis(0) < -0.1 else 0
        self.Move(eng.RIGHT * self.speed * eng.Engine.Instance.deltaTime * -rotZ)

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
        if keys[pg.K_SPACE] or self.joystick.get_button(0):
            self.Atk()
        #rechargement
        if keys[pg.K_r]:
            if self.mun < 6 and self.mun >= 0:
                self.mun = 6
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

        if((keys[pg.K_e] or self.joystick.get_button(1)) and self.lastTimeVueSwitch + 300 < eng.Engine.Instance.time):
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
            self.Dmg(-1)
            self.cheatLifeUp = 1
        elif keys[pg.K_p] == False and self.cheatLifeUp == 1:
            self.cheatLifeUp = 0
        if keys[pg.K_m] and self.cheatLifeDown == 0:
            self.Dmg(1)
            self.cheatLifeDown = 1
        elif keys[pg.K_m] == False and self.cheatLifeDown == 1:
            self.cheatLifeDown = 0
        #Cheat code start
        if keys[pg.K_a]:

            self.position.z = 0
            self.rotation = glm.vec3([0, 0, 0])
        else:
        #Cheat code end
            self.Move(eng.FORWARD * self.scrollSpeed * eng.Engine.Instance.deltaTime)
            
            maxAngle = 25
            if(self.rotation[0] > maxAngle or self.rotation[0] < -maxAngle) : rotX = 0
            if(self.rotation[2] > maxAngle or self.rotation[2] < -maxAngle) : rotZ = 0
            
            if(rotX == 0):
                if(self.rotation[0] > 3 and keys[pg.K_z] == False and self.joystick.get_axis(1) > -0.1) :rotX += -1
                elif(self.rotation[0] < -3 and keys[pg.K_s] == False and self.joystick.get_axis(1) < 0.1) : rotX += 1
            if(rotZ == 0):
                if(self.rotation[2] > 3 and keys[pg.K_d] == False and self.joystick.get_axis(0) < 0.1) : rotZ += -1
                elif(self.rotation[2] < -3 and keys[pg.K_q] == False and self.joystick.get_axis(0) > -0.1) : rotZ += 1

            self.Rotate(self.rotSpeed * eng.Engine.Instance.deltaTime, glm.vec3([rotX, rotY, rotZ]))
        
        if self.position.x >= 100:
            self.position.x = 100
        elif self.position.x <= -100:
            self.position.x = -100
        
        if self.position.y >= 100:
            self.position.y = 100
        elif self.position.y <= -100:
            self.position.y = -100

        eng.Engine.Instance.graphicEngine.camera.position = self.position + self.cameraOffset
        if(self.vue == 1) : self.SetRotCamera((0, 90, 0))
        self.guiPlayer.LifePlayer(self.life, self.mun)

        super().Update()