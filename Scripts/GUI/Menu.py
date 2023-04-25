import pygame as pg
import sys
from PIL import Image
from Engine.GameObject import GameObject
from Engine.Engine import Engine
from dependencies.parsejson.parse import *

pause_buttons = pg.sprite.Group()
option_buttons = pg.sprite.Group()

class Button(pg.sprite.Sprite):
            def __init__(self, x, y, w, h, path_txt, txtSize, Engine, list, jsonPath):
                super().__init__()

                self.engine = Engine

                self.x = x
                self.y = y
                self.w = w
                self.h = h

                self.jsonPath = jsonPath
                self.texturePath = ASSETS[self.jsonPath[0]][self.jsonPath[1]][self.jsonPath[2]]
                self.loadTexture = pg.image.load(self.texturePath).convert_alpha()
                self.loadTexture = pg.transform.scale(self.loadTexture, (self.w,self.h))

                self.path_txt = path_txt
                self.text = self.engine.Dialog[self.path_txt[0]][self.path_txt[1]][self.path_txt[2]]

                self.txtSize = txtSize
                self.colors = "black"
                self.font = pg.font.SysFont("Arial", self.txtSize)
                self.text_render = self.font.render(self.text, 1, "white")
                self.image = self.text_render
                self.txt_x, self.txt_y, self.txt_w , self.txt_h = self.text_render.get_rect()

                self.im = Image.open(self.texturePath)

                
                

                self.rect = pg.Rect(self.x + (self.w - self.txt_w) / 2, self.y + (self.h - self.txt_h) / 2, self.w, self.h)
                self.rectTexture = pg.Rect(self.x, self.y, self.w, self.h)

                self.engine.window.blit(self.loadTexture,self.rectTexture)
                
                self.update()
                list.add(self)

                

            def update(self):
                self.texturePath = ASSETS[self.jsonPath[0]][self.jsonPath[1]][self.jsonPath[2]]
                self.loadTexture = pg.image.load(self.texturePath).convert_alpha()
                self.loadTexture = pg.transform.scale(self.loadTexture, (self.w,self.h))
                self.font = pg.font.SysFont("Arial", self.txtSize)
                self.text_render = self.font.render(self.text, 1, "white")
                self.image = self.text_render
                self.txt_x, self.txt_y, self.txt_w , self.txt_h = self.text_render.get_rect()
                self.rect = pg.Rect(self.x + (self.w - self.txt_w) / 2, self.y + (self.h - self.txt_h) / 2, self.w, self.h)
                self.rectTexture = pg.Rect(self.x, self.y, self.w, self.h)
                self.engine.window.blit(self.loadTexture,self.rectTexture)
                



class Menu(GameObject):

    def __init__(self, engine, position = [0, 0, 0], rot = [0, 0, 0], scale = [0, 0, 0]):
        super().__init__(position,rot,scale)

        self.onoff = "on"
        self.statut = "pause"
        self.engine = engine
        self.window = engine.window

        self.pause_buttons = pause_buttons
        self.option_buttons = option_buttons

        # Pause menu
        button_w = 271
        button_h = 85
        button_x = (self.engine.wW - button_w) / 2

        spaceBetween = (self.engine.wH - (button_h * 3)) / 4

        btn1_y = spaceBetween
        btn2_y = spaceBetween + (button_h + spaceBetween)
        btn3_y = spaceBetween + (button_h + spaceBetween) * 2

        # self.pause_b0 = Button(button_x, btn1_y, button_w, button_h, ("menu", "pause", "resume_btn"), 45, self.engine, self.pause_buttons)
        # self.pause_b1 = Button(button_x, btn2_y, button_w, button_h, ("menu", "pause", "options_btn"), 45, self.engine, self.pause_buttons)
        self.pause_resume = Button(button_x, btn3_y, button_w, button_h, ("menu", "pause", "exit_btn"), 45, self.engine, self.pause_buttons, ["guiMenu", "exitButton", "normal"])

        # # Option menu
        # self.option_backB = Button(self.engine.wW * 0.02, self.engine.wH * 0.02, button_w, button_h, ("menu", "option", "back_btn") , 45, self.engine,self.option_buttons)

        # self.option_frB = Button(button_x - button_w / 2, btn1_y, button_w, button_h, ("menu", "option", "fr_btn"), 45, self.engine,self.option_buttons)
        # self.option_enB = Button(button_x + button_w / 2, btn1_y, button_w, button_h, ("menu", "option", "en_btn"), 45, self.engine,self.option_buttons)


        
    def not_hover(self):
        for x in self.pause_buttons:
            x.jsonPath[2] = "normal"
            x.update()
        for x in self.option_buttons:
            x.jsonPath[2] = "normal"
            x.update()

    def hover(self, button):
        button.jsonPath[2] = "hover"
        #Flèche hover
        #Left
        leftArrow_texturePath = ASSETS["guiMenu"]["hoverButtonArrow"]["right"]
        leftArrow_loadTexture = pg.image.load(leftArrow_texturePath).convert_alpha()
        leftArrow_size = Image.open(leftArrow_texturePath)
        leftArrow_w, leftArrow_h = leftArrow_size.size
        rectLeftArrow = pg.Rect(button.x - leftArrow_w - 10, button.y - (leftArrow_h - button.h) / 2, leftArrow_w, leftArrow_h)
        self.engine.window.blit(leftArrow_loadTexture,rectLeftArrow)
        #Right
        rightArrow_texturePath = ASSETS["guiMenu"]["hoverButtonArrow"]["left"]
        rightArrow_loadTexture = pg.image.load(rightArrow_texturePath).convert_alpha()
        rightArrow_size = Image.open(rightArrow_texturePath)
        rightArrow_w, rightArrow_h = rightArrow_size.size
        rectRightArrow = pg.Rect(button.x + button.w + 10, button.y - (leftArrow_h - button.h) / 2, rightArrow_w, rightArrow_h)
        self.engine.window.blit(rightArrow_loadTexture,rectRightArrow)
        button.update()

    def txt_btn_update(self):
        for x in self.pause_buttons:
            x.text = self.engine.Dialog[x.path_txt[0]][x.path_txt[1]][x.path_txt[2]]
            x.update()
            print(x.text)
        for x in self.option_buttons:
            x.text = self.engine.Dialog[x.path_txt[0]][x.path_txt[1]][x.path_txt[2]]
            x.update()
            print(x.text)


            

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
                    # if self.pause_b0.rect.collidepoint(pg.mouse.get_pos()) and event.type == pg.MOUSEBUTTONDOWN and event.button==1:
                    #     self.onoff = "off"

                    # if self.pause_b1.rect.collidepoint(pg.mouse.get_pos()) and event.type == pg.MOUSEBUTTONDOWN and event.button==1:
                    #     self.statut = "option"

                    if self.pause_resume.rectTexture.collidepoint(pg.mouse.get_pos()) and event.type == pg.MOUSEBUTTONDOWN and event.button==1:
                        pg.quit()
                        sys.exit()

                    if event.type == pg.MOUSEMOTION:

                        # if self.pause_b0.rect.collidepoint(pg.mouse.get_pos()):
                        #     self.pause_b0.colors = "white"
                        # elif self.pause_b1.rect.collidepoint(pg.mouse.get_pos()):
                        #     self.pause_b1.colors = "white"
                        if self.pause_resume.rectTexture.collidepoint(pg.mouse.get_pos()):
                            self.hover(self.pause_resume)
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
                            self.txt_btn_update()
                            

                    elif self.option_enB.rect.collidepoint(pg.mouse.get_pos()) and event.type == pg.MOUSEBUTTONDOWN and event.button==1:
                        if self.engine.Ln != "en":
                            self.engine.Ln = "en"
                            self.engine.Dialog = loadDialog("en")
                            self.txt_btn_update()


                    
                    if event.type == pg.MOUSEMOTION:

                        if self.option_backB.rect.collidepoint(pg.mouse.get_pos()):
                            self.hover()
                        elif self.option_frB.rect.collidepoint(pg.mouse.get_pos()):
                            self.hover()
                        elif self.option_enB.rect.collidepoint(pg.mouse.get_pos()):
                            self.hover()

                        else:
                            self.not_hover()

                    self.option_buttons.update()
                    self.option_buttons.draw(self.engine.window)


                
                    
                    
                        









                

        
        

