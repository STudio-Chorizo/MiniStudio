import dependencies.engine.engine as eng
from dependencies.engine.gameobject import *
from dependencies.endlvl.endlvl import *

class EndObj(GameObject):
    def __init__(self, pos=..., rot=..., scale=...):
        super().__init__(pos, rot, scale)
        self.obj = None

    def Update(self):
        self.LookAt(eng.Engine.Instance.gameObjects["0"].position)
        return super().Update()
    
    def OnCollide(self, colider):
        if colider.UID != "0":
            return
        print("je suis touche")
        self.EndN()

    def EndN(self):
        print("OPEN")
        dino = EndLvl()
        dino.NewLvl(eng.Engine.Instance.lvl)
        eng.Engine.Instance.lvl + 1
        