from dependencies.scripts.entities.entities import Entities
import dependencies.engine.engine as eng
import pygame as pg
from dependencies.parsejson.parse import *

class Bullet(Entities):
    def __init__(self, name, pos=..., rot=..., scale=...):
        super().__init__(name, pos, rot, scale)
        self.speed = 0.1
    
    def Update(self):
        if(self.position[2] < eng.Engine.Instance.player.position[2] - 100):
            self.Destroy()
            return
        self.Move(eng.FORWARD * self.speed * eng.Engine.Instance.deltaTime)
        return super().Update()