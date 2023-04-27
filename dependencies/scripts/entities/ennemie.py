

import dependencies.engine.engine as eng
from dependencies.scripts.entities.entities import Entities


class Ennemie(Entities):
    def __init__(self, name, reloadTime = 1, pos=..., rot=..., scale=...):
        super().__init__(name, reloadTime, pos, rot, scale)

    def OnCollide(self, colider):
        return super().OnCollide(colider)
    
    def Update(self):
        self.LookAt(eng.Engine.Instance.player.position)
        if(self.lastAtk + self.reload < eng.Engine.Instance.time) :
            self.Atk()
        return super().Update()
    
    