import pygame as pg
import sys
from Engine.GameObject import GameObject
from Engine.Engine import Engine
from dependencies.parsejson.parse import *

pause_buttons = pg.sprite.Group()
option_buttons = pg.sprite.Group()

class Button(pg.sprite.Sprite):
            def __init__(self, x, y, w, h, text, size, Engine, list):
                super().__init__()
                self.engine = Engine
                self.colors = "black"
                self.text = text
                self.font = pg.font.SysFont("Arial", size)
                self.text_render = self.font.render(text, 1, "white")
                self.image = self.text_render
                self.txt_x, self.txt_y, self.txt_w , self.txt_h = self.text_render.get_rect()

                self.x = x
                self.y = y
                self.w = w
                self.h = h

                self.rect = pg.Rect(self.x + (self.w - self.txt_w) / 2, self.y + (self.h - self.txt_h) / 2, self.w, self.h)
                
                self.update()
                list.add(self)

                

            def update(self):
                pg.draw.rect(self.engine.window, self.colors, (self.x, self.y, self.w, self.h),5, 10)
                



class Menu(GameObject):

    def __init__(self, engine, position = [0, 0, 0], rot = [0, 0, 0], scale = [0, 0, 0]):
        super().__init__(position,rot,scale)

        self.onoff = "off"
        self.statut = "pause"
        self.engine = engine
        self.window = engine.window

        self.pause_buttons = pause_buttons
        self.option_buttons = option_buttons

        # Pause menu
        button_w = self.engine.wW * 0.3
        button_h = self.engine.wH * 0.1
        button_x = (self.engine.wW - button_w) / 2

        spaceBetween = (self.engine.wH - (button_h * 3)) / 4

        btn1_y = spaceBetween
        btn2_y = spaceBetween + (button_h + spaceBetween)
        btn3_y = spaceBetween + (button_h + spaceBetween) * 2

        self.pause_b0 = Button(button_x, btn1_y, button_w, button_h, self.engine.Dialog["menu"]["pause"]["resume_btn"], 45, self.engine,self.pause_buttons)
        self.pause_b1 = Button(button_x, btn2_y, button_w, button_h, self.engine.Dialog["menu"]["pause"]["options_btn"], 45, self.engine,self.pause_buttons)
        self.pause_b2 = Button(button_x, btn3_y, button_w, button_h, self.engine.Dialog["menu"]["pause"]["exit_btn"], 45, self.engine,self.pause_buttons)

        # Option menu
        self.option_backB = Button(self.engine.wW * 0.02, self.engine.wH * 0.02, button_w, button_h, self.engine.Dialog["menu"]["option"]["back_btn"] , 45, self.engine,self.option_buttons)

        self.option_frB = Button(button_x - button_w / 2, btn1_y, button_w, button_h, self.engine.Dialog["menu"]["option"]["fr_btn"], 45, self.engine,self.option_buttons)
        self.option_enB = Button(button_x + button_w / 2, btn1_y, button_w, button_h, self.engine.Dialog["menu"]["option"]["en_btn"], 45, self.engine,self.option_buttons)


        
    def not_hover(self):
        for x in self.pause_buttons:
            x.colors = "black"
            x.update()
        for x in self.option_buttons:
            x.colors = "black"
            x.update()


            

    def Update(self):
        for event in pg.event.get():

            self.window.fill((0,0,0))

            if event.type == pg.QUIT:
                 pg.quit()
                 sys.exit()       

            if (event.type == pg.KEYDOWN):
                if event.key == pg.K_ESCAPE:

                    if self.onoff == "off":
                        self.onoff = "on"

                    elif self.onoff == "on":

                        if self.statut == "pause":
                            self.onoff = "off"

                        if self.statut == "option":
                            self.statut = "pause"
                            



            if (self.onoff == "on"):

                if self.statut == "pause":
                    if self.pause_b0.rect.collidepoint(pg.mouse.get_pos()) and event.type == pg.MOUSEBUTTONDOWN and event.button==1:
                        self.onoff = "off"

                    if self.pause_b1.rect.collidepoint(pg.mouse.get_pos()) and event.type == pg.MOUSEBUTTONDOWN and event.button==1:
                        self.statut = "option"

                    if self.pause_b2.rect.collidepoint(pg.mouse.get_pos()) and event.type == pg.MOUSEBUTTONDOWN and event.button==1:
                        pg.quit()
                        sys.exit()

                    if event.type == pg.MOUSEMOTION:

                        if self.pause_b0.rect.collidepoint(pg.mouse.get_pos()):
                            self.pause_b0.colors = "white"
                        elif self.pause_b1.rect.collidepoint(pg.mouse.get_pos()):
                            self.pause_b1.colors = "white"
                        elif self.pause_b2.rect.collidepoint(pg.mouse.get_pos()):
                            self.pause_b2.colors = "white"
                        else:
                            self.not_hover()
                        
                    self.pause_buttons.update()
                    self.pause_buttons.draw(self.engine.window)
                
                if self.statut == "option":

                    if self.option_backB.rect.collidepoint(pg.mouse.get_pos()) and event.type == pg.MOUSEBUTTONDOWN and event.button==1:
                        self.statut = "pause"

                    elif self.option_frB.rect.collidepoint(pg.mouse.get_pos()) and event.type == pg.MOUSEBUTTONDOWN and event.button==1:
                        if self.engine.Ln != "fr":
                            self.engine.Ln = "fr"
                            self.engine.Dialog = loadDialog("fr")
                            self.pause_b0.text = 

                    elif self.option_enB.rect.collidepoint(pg.mouse.get_pos()) and event.type == pg.MOUSEBUTTONDOWN and event.button==1:
                        if self.engine.Ln != "en":
                            self.engine.Ln = "en"
                            self.engine.Dialog = loadDialog("en")


                    
                    if event.type == pg.MOUSEMOTION:

                        if self.option_backB.rect.collidepoint(pg.mouse.get_pos()):
                            self.option_backB.colors = "white"
                        elif self.option_frB.rect.collidepoint(pg.mouse.get_pos()):
                            self.option_frB.colors = "white"
                        elif self.option_enB.rect.collidepoint(pg.mouse.get_pos()):
                            self.option_enB.colors = "white"

                        else:
                            self.not_hover()

                    self.option_buttons.update()
                    self.option_buttons.draw(self.engine.window)

                
                    
                    
                        









                

        
        

