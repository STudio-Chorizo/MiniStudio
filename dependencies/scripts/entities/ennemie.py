

from dependencies.scripts.entities.entities import Entities


class Ennemie(Entities):
    def __init__(self, pos=..., rot=..., scale=...):
        super().__init__(pos, rot, scale)

    def OnCollide(self, colider):
        return super().OnCollide(colider)
    
    def Update(self):
        return super().Update()
    
    