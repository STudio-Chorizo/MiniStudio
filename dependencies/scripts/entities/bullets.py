import glm
from dependencies.engine.Untils.vector import Magnitude
from dependencies.engine.gameobject import GameObject
import dependencies.engine.engine as eng
from dependencies.parsejson.parse import *
import dependencies.scripts.entities.entities as ent

class Bullet(GameObject):
    def __init__(self, name, pos=..., rot=..., scale=...):
        super().__init__(name, pos, rot, scale)
        self.speed = 0.2
        self.ally = None
        self.start = 0
    
    def Shoot(self, ally, start, rot):
        self.speed = 0.02
        self.ally = ally
        self.position = start
        self.start = start
        self.rotation = glm.vec3(rot)

    def OnCollide(self, colider):
        if(ent.Entities.IsEntities(colider) == True) : 
            if(self.ally == colider.UID): return
            colider.Dmg(1)
        super().OnCollide(colider)

    def Update(self):
        if(super().Update() == False) : return
        if(Magnitude(self.position - self.start) > 150) : 
            eng.Engine.Instance.Destroy(self.UID)
            return
        self.Move(self.forward * self.speed * eng.Engine.Instance.deltaTime)