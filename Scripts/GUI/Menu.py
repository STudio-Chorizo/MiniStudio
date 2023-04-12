import pygame as pg
from button import button
from Engine.GameObject import GameObject



class Menu(GameObject):

    def __init__(self, position = [0, 0, 0], rot = [0, 0, 0], scale = [0, 0, 0]):
        super.__init__(position,rot,scale)








    def Update(self, Engine):
        Engine.window.fill("black")

