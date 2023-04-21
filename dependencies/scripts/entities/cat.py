import dependencies.engine.engine as eng
from dependencies.engine.gameobject import *
from dependencies.endlvl.endlvl import *

class Cat(GameObject):
    def __init__(self, pos=..., rot=..., scale=...):
        super().__init__(pos, rot, scale)

    def Update(self):
        self.LookAt(eng.Engine.Instance.gameObjects["0"].position)
        return super().Update()
    
