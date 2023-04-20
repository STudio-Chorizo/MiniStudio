import dependencies.engine.engine as eng
from dependencies.engine.gameobject import GameObject
from dependencies.scripts.entities.ennemie import Ennemie


class Spawn(GameObject):
    def __init__(self, CD = 10, pos=..., rot=..., scale=...):
        super().__init__(pos, rot, scale)
        self.coolDown = CD
        self.lastTime = eng.Engine.Instance.time

    def Update(self):
        if(self.position[2] < eng.Engine.Instance.gameObjects["0"].position[2] + 100) :
            #self.Destroy()
            return
        if(self.lastTime + self.coolDown < eng.Engine.Instance.time) :
            #Use pool to spawn ennemie
            pass
        return super().Update()
    
