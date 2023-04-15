import dependencies.engine.engine as eng
from dependencies.engine.gameobject import *
import glm
import pygame as pg

class Player(GameObject):
    def __init__(self, pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1)):
        self.vue = 3
        self.right = glm.vec3(1, 0, 0)
        self.up = glm.vec3(0, 1, 0)
        self.forward = glm.vec3(0, 0, 1)
        self.speed = 0.01
        self.scrollSpeed = 0.03
        super().__init__(pos, rot, scale)
        eng.Engine.Instance.graphicEngine.camera.target = self

    def OnCollide(self, colider):
        print("["+pg.time.get_ticks().__str__()+"] Lost")
        return super().OnCollide(colider)

    def Update(self):
        keys = pg.key.get_pressed()
        rotX = 0
        rotY = 0
        rotZ = 0
        if keys[pg.K_z]:
            self.Move(self.up * self.speed * eng.Engine.Instance.deltaTime)
            rotX = 0.4
        if keys[pg.K_s]:
            self.Move(-self.up * self.speed * eng.Engine.Instance.deltaTime)
            rotX = -0.4
        if keys[pg.K_q]:
            self.Move(-self.right * self.speed * eng.Engine.Instance.deltaTime)
            rotZ = 0.4
        if keys[pg.K_d]:
            self.Move(self.right * self.speed * eng.Engine.Instance.deltaTime)
            rotZ = -0.4
        
        self.Move(self.forward * self.scrollSpeed * eng.Engine.Instance.deltaTime)
        self.SetRot(glm.vec3([rotX, rotY, rotZ]))

        if self.vue == 3:
            self.SyncPosCamera()
        elif self.vue == 1:
            self.SyncPosCamera(glm.vec3([0, 0.0, -0.1]))
            self.SyncRotCamera((-90, 0, 0))

        super().Update()