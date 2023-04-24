
from dependencies.engine.gameobject import *

class Entities(GameObject):
    def __init__(self, pos=..., rot=..., scale=...):
        super().__init__(pos, rot, scale)
        self.speed = 0.01
        self.rotSpeed = 0.003
        self.life = 3

    def OnCollide(self, colider):
        return super().OnCollide(colider)
    
    def Update(self):
        return super().Update()
    
    def Atk(self):
        pass

    def Dmg(self, dmg):
        self.life -= dmg
        if(self.life <= 0) : self.Die()

    def Die(self):
        #self.Destroy()
        pass