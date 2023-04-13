from dependencies.engine.engine import *
from dependencies.engine.gameobject import *
import glm

class Player(GameObject):
    def __init__(self, pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1)):
        self.right = glm.vec3(1, 0, 0)
        self.up = glm.vec3(0, 1, 0)
        self.forward = glm.vec3(0, 0, -1)
        self.speed = 0.01
        super().__init__(pos, rot, scale)
        Engine.Instance.graphicEngine.camera.target = self

    def Update(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_z]:
            self.Move(self.up * self.speed * Engine.Instance.deltaTime)
        elif keys[pg.K_s]:
            self.Move(-self.up * self.speed * Engine.Instance.deltaTime)
        elif keys[pg.K_q]:
            self.Move(-self.right * self.speed * Engine.Instance.deltaTime)
        elif keys[pg.K_d]:
            self.Move(self.right * self.speed * Engine.Instance.deltaTime)
        
        self.Move(self.forward * self.speed * Engine.Instance.deltaTime)

        self.model.m_model = self.model.get_model_matrix()