import pygame as pg
from Engine.GameObject import GameObject
from Engine.Engine import Engine



class Menu(GameObject):

    def __init__(self, engine, position = [0, 0, 0], rot = [0, 0, 0], scale = [0, 0, 0]):
        super().__init__(position,rot,scale)

        self.window = engine.window
        self.window_wW = engine.wW
        self.window_wH = engine.wH
        self.btn = 0
        self.btn_h = self.window_wH*0.1
        self.btn_w = self.window_wW*0.1





    def Update(self, Engine):
        self.btn = pg.draw.rect(self.window,(170,170,170),[(self.window_wW/2)-self.btn_w/2, (self.window_wH/2)-self.btn_h/2, self.btn_w,self.btn_h])
        pg.display.update()

