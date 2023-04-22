import dependencies.engine.engine as eng
from dependencies.engine.gameobject import *
import glm
import pygame as pg

class Player(GameObject):
    def __init__(self, pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1)):
        self.vue = 0
        self.lastTimeVueSwitch = 0
        self.right = glm.vec3(1, 0, 0)
        self.up = glm.vec3(0, 1, 0)
        self.forward = glm.vec3(0, 0, 1)
        self.speed = 0.01
        self.rotSpeed = 0.003
        self.scrollSpeed = 0.03
        super().__init__(pos, rot, scale)
        self.cameraOffset = glm.vec3([0, 0.15, -0.2])
        self.SetRotCamera((-10, 90, 0))

    def SetRotCamera(self, camOrientation: tuple = (0, 0, 0), local = True) -> None:
        cam = Eng.Engine.Instance.graphicEngine.camera
        rot = camOrientation
        if(local == True) : rot += self.rotation
        cam.pitch = rot[0]
        cam.yaw = rot[1]
        cam.roll = rot[2]

    def OnCollide(self, colider):
        print("["+pg.time.get_ticks().__str__()+"] Lost")
        return super().OnCollide(colider)

    def Update(self):
        keys = pg.key.get_pressed()
        rotX = 0
        rotY = 0
        rotZ = 0
        #Position
        if keys[pg.K_z]:
            self.Move(self.up * self.speed * eng.Engine.Instance.deltaTime)
            rotX = 1
        if keys[pg.K_s]:
            self.Move(-self.up * self.speed * eng.Engine.Instance.deltaTime)
            rotX = -1
        if keys[pg.K_d]:
            self.Move(-self.right * self.speed * eng.Engine.Instance.deltaTime)
            rotZ = 1
        if keys[pg.K_q]:
            self.Move(self.right * self.speed * eng.Engine.Instance.deltaTime)
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
        else:
        #Cheat code end
            self.Move(self.forward * self.scrollSpeed * eng.Engine.Instance.deltaTime)
            
            maxAngle = math.pi / 4
            if(self.rotation[0] > maxAngle or self.rotation[0] < -maxAngle) : rotX = 0
            if(self.rotation[2] > maxAngle or self.rotation[2] < -maxAngle) : rotZ = 0
            
            if(rotX == 0 and (keys[pg.K_z] or keys[pg.K_s]) == False):
                if(self.rotation[0] > 0.06) : rotX = -1 
                #elif(self.rotation[0] > 0) : self.Rotate(-round(self.rotation[0], 2) * eng.Engine.Instance.deltaTime, (1, 0, 0))
                elif(self.rotation[0] < -0.06) : rotX = 1
                #else : self.Rotate(round(self.rotation[0], 2) * eng.Engine.Instance.deltaTime, (1, 0, 0))
            if(rotZ == 0 and (keys[pg.K_q] or keys[pg.K_d]) == False):
                if(self.rotation[2] > 0.06) : rotZ = -1
                #elif(self.rotation[2] > 0) : self.Rotate(-round(self.rotation[2], 2) * eng.Engine.Instance.deltaTime, (0, 0, 1))
                elif(self.rotation[2] < -0.06) : rotZ = 1
                #else : self.Rotate(round(self.rotation[2], 2) * eng.Engine.Instance.deltaTime, (0, 0, 1))

            self.Rotate(self.rotSpeed * eng.Engine.Instance.deltaTime, glm.vec3([rotX, rotY, rotZ]))

        print(self.cameraOffset)
        Eng.Engine.Instance.graphicEngine.camera.position = self.position + self.cameraOffset
        if(self.vue == 1) : self.SetRotCamera((0, 90, 0))

        super().Update()