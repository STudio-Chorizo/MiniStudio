import pygame as pg
import sys
from Engine.GameObject import GameObject
from Engine.Engine import Engine

buttons = pg.sprite.Group()

class Button(pg.sprite.Sprite):
            def __init__(self, w, h, y, text, size, Engine, list):
                super().__init__()
                self.engine = Engine
                self.colors = "black"
                self.font = pg.font.SysFont("Arial", size)
                self.text_render = self.font.render(text, 1, "white")
                self.image = self.text_render
                self.txt_x, self.txt_y, self.txt_w , self.txt_h = self.text_render.get_rect()

                self.w = self.engine.wW * w
                self.h = self.engine.wH * h
                self.x = (self.engine.wW - self.w) / 2
                self.y = y

                self.rect = pg.Rect(self.x + (self.w - self.txt_w) / 2, self.y + (self.h - self.txt_h) / 2, self.w, self.h)
                self.update()
                list.add(self)

            def update(self):
                # self.x = (self.w - self.txt_w) / 2
                pg.draw.rect(self.engine.window, self.colors, (self.x, self.y, self.w, self.h),5, 10)
                



class Menu(GameObject):

    def __init__(self, engine, position = [0, 0, 0], rot = [0, 0, 0], scale = [0, 0, 0]):
        super().__init__(position,rot,scale)

        self.statut = "off"
        self.engine = engine
        self.window = engine.window

        self.buttons = buttons

        button_h = 0.1
        button_w = 0.3

        spaceBetween = (self.engine.wH - (self.engine.wH * button_h)) / 4

        self.btn1_y = spaceBetween
        self.btn2_y = spaceBetween + 1 * (button_w + spaceBetween)
        self.btn3_y = spaceBetween + 2 * (button_w + spaceBetween)

        self.b0 = Button(button_w, button_h, self.btn1_y , "Resume", 45, self.engine,self.buttons)
        self.b1 = Button(button_w, button_h, self.btn2_y , "Option", 45, self.engine,self.buttons)
        self.b2 = Button(button_w, button_h, self.btn3_y , "Exit", 45, self.engine,self.buttons)

    def not_hover(self):
        for x in self.buttons:
            x.colors = "black"
            x.update()



    def Update(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                 pg.quit()
                 sys.exit()       

            if (event.type == pg.KEYDOWN):
                if event.key == pg.K_ESCAPE:   
                    if self.statut == "on":
                        self.statut = "off"
                        self.window.fill((0,0,0))
                    elif self.statut == "off":
                        self.statut = "on"

            if (self.statut == "on"):

                if self.b2.rect.collidepoint(pg.mouse.get_pos()) and event.type == pg.MOUSEBUTTONDOWN and event.button==1:
                    pg.quit()
                    sys.exit()

                if self.b0.rect.collidepoint(pg.mouse.get_pos()) and event.type == pg.MOUSEBUTTONDOWN and event.button==1:
                    self.statut = "off"
                    self.window.fill((0,0,0))
                    return(0)
                    
                    

                if event.type == pg.MOUSEMOTION:
                    # 2. put the collide check for mouse hover here for each button
                    if self.b0.rect.collidepoint(pg.mouse.get_pos()):
                        self.b0.colors = "white"
                    elif self.b1.rect.collidepoint(pg.mouse.get_pos()):
                        self.b1.colors = "white"
                    elif self.b2.rect.collidepoint(pg.mouse.get_pos()):
                        self.b2.colors = "white"
                    else:
                        # this will work for every buttons going back to original color after mouse goes out
                        self.not_hover()
                    
                self.buttons.update()
                self.buttons.draw(self.engine.window)

        
        

