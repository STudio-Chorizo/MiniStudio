import pygame as pg
from button import button
from Engine.GameObject import GameObject



class Menu(GameObject):

    def __init__(self, engine, position = [0, 0, 0], rot = [0, 0, 0], scale = [0, 0, 0]):
        super.__init__(position,rot,scale)

        self.window = engine.window








    def Update(self, Engine):
        self.window.fill("black")
        pg.display.update()

