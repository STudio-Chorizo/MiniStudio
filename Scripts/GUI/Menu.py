import pygame as pg
import sys
from PIL import Image
from Engine.GameObject import GameObject
from Engine.Engine import Engine
from dependencies.parsejson.parse import *

main_buttons = pg.sprite.Group()
pause_buttons = pg.sprite.Group()
options_buttons = pg.sprite.Group()

class Button(pg.sprite.Sprite):
            def __init__(self, x, y, h, path_txt, txtSize, Engine, list, jsonPath):
                super().__init__()

                self.engine = Engine

                self.x = x
                self.y = y

                self.jsonPath = jsonPath
                self.texturePath = ASSETS[self.jsonPath[0]][self.jsonPath[1]][self.jsonPath[2]][self.jsonPath[3]]
                self.loadTexture = pg.image.load(self.texturePath).convert_alpha()

                im = Image.open(self.texturePath)
                self.w, self.h = im.size
                self.ratio = self.w/self.h
                self.h = round(h)
                self.w = round(self.h * self.ratio)

                self.loadTexture = pg.transform.scale(self.loadTexture, (self.w,self.h))

                self.path_txt = path_txt
                if self.path_txt != "":
                    self.text = self.engine.Dialog[self.path_txt[0]][self.path_txt[1]][self.path_txt[2]]
                else :
                    self.text = ""

                self.txtSize = txtSize
                self.colors = "black"
                self.font = pg.font.Font("Assets/font/Orbitron-Black.ttf", self.txtSize)
                self.text_render = self.font.render(self.text, 1, "white")
                self.image = self.text_render
                self.txt_x, self.txt_y, self.txt_w , self.txt_h = self.text_render.get_rect()

                self.rect = pg.Rect(self.x + (self.w - self.txt_w) / 2, self.y + (self.h - self.txt_h) / 2, self.w, self.h)
                self.rectTexture = pg.Rect(self.x, self.y, self.w, self.h)

                self.engine.window.blit(self.loadTexture,self.rectTexture)
                
                self.update()
                list.add(self)

                

            def update(self):
                self.texturePath = ASSETS[self.jsonPath[0]][self.jsonPath[1]][self.jsonPath[2]][self.jsonPath[3]]
                self.loadTexture = pg.image.load(self.texturePath).convert_alpha()
                self.loadTexture = pg.transform.scale(self.loadTexture, (self.w,self.h))
                self.font = pg.font.Font("Assets/font/Orbitron-Black.ttf", self.txtSize)
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

        self.main_buttons = main_buttons
        self.pause_buttons = pause_buttons
        self.option_buttons = options_buttons

        #----------------Main menu-------------------
        self.backgroundPath = ASSETS["guiMenu"]["main"]["background"]
        self.loadBackground = pg.image.load(self.backgroundPath).convert_alpha()
        self.main_backgroudRect = pg.Rect(0, 0, self.engine.wW, self.engine.wH)
        self.main_loadBackground = pg.transform.scale(self.loadBackground, (self.engine.wW,self.engine.wH))
        self.engine.window.blit(self.main_loadBackground,self.main_backgroudRect)

        main_topmarge = 0.24
        
        main_button_x = self.engine.wW * 0.05
        main_button_h = self.engine.wH * 0.05
        main_txtsize = 25
        main_spaceBetween = ((self.engine.wH - self.engine.wH * main_topmarge) - (main_button_h * 6)) / 7
        
        self.engine.wH * main_topmarge + main_spaceBetween + (main_button_h + main_spaceBetween)* 0

        self.main_play = Button(main_button_x, self.engine.wH * main_topmarge + main_spaceBetween + (main_button_h + main_spaceBetween)* 0, main_button_h, ("menu", "main", "play_btn"), main_txtsize, self.engine, self.main_buttons, ["guiMenu", "main", "playButton", "normal"])
        self.main_newGame = Button(main_button_x, self.engine.wH * main_topmarge + main_spaceBetween + (main_button_h + main_spaceBetween)* 1, main_button_h, ("menu", "main", "newGame_btn"), main_txtsize, self.engine, self.main_buttons, ["guiMenu", "main", "newGameButton", "normal"])
        self.main_leaderboard = Button(main_button_x, self.engine.wH * main_topmarge + main_spaceBetween + (main_button_h + main_spaceBetween)* 2, main_button_h, ("menu", "main", "leaderboard_btn"), main_txtsize, self.engine, self.main_buttons, ["guiMenu", "main", "leaderboardButton", "normal"])
        self.main_saves = Button(main_button_x, self.engine.wH * main_topmarge + main_spaceBetween + (main_button_h + main_spaceBetween)* 3, main_button_h, ("menu", "main", "saves_btn"), main_txtsize, self.engine, self.main_buttons, ["guiMenu", "main", "savesButton", "normal"])
        self.main_options = Button(main_button_x, self.engine.wH * main_topmarge + main_spaceBetween + (main_button_h + main_spaceBetween)* 4, main_button_h, ("menu", "main", "options_btn"), main_txtsize, self.engine, self.main_buttons, ["guiMenu", "main", "optionsButton", "normal"])
        self.main_exit = Button(main_button_x, self.engine.wH * main_topmarge + main_spaceBetween + (main_button_h + main_spaceBetween)* 5, main_button_h, ("menu", "main", "exit_btn"), main_txtsize, self.engine, self.main_buttons, ["guiMenu", "main", "exitButton", "normal"])

        #----------------Pause menu-------------------
        #Background Filter
        self.pause_BgFilterPath = ASSETS["guiMenu"]["pause"]["background"]
        self.pause_loadBgFilter = pg.image.load(self.pause_BgFilterPath).convert_alpha()
        self.pause_BgFilterRect = pg.Rect(0, 0, self.engine.wW, self.engine.wH)
        self.pause_loadBgFilter = pg.transform.scale(self.pause_loadBgFilter, (self.engine.wW,self.engine.wH))
        self.engine.window.blit(self.pause_loadBgFilter,self.pause_BgFilterRect)

        #Window skin
        self.pause_windowPath = ASSETS["guiMenu"]["pause"]["window"]
        self.pause_loadWindow = pg.image.load(self.pause_windowPath).convert_alpha()
        pause_window = Image.open(self.pause_windowPath)
        window_w, window_h = pause_window.size
        self.pause_windowRect = pg.Rect((self.engine.wW - window_w)/2, (self.engine.wH - window_h)/2, window_w, window_h)
        self.pause_loadWindow = pg.transform.scale(self.pause_loadWindow, (window_w, window_h))
        self.engine.window.blit(self.pause_loadWindow,self.pause_windowRect)

        #Buttons
        pauseBtn = Image.open(ASSETS["guiMenu"]["pause"]["resumeButton"]["normal"])
        pauseBtn_w, pauseBtn_h = pauseBtn.size
        pauseBtn_w = round(pauseBtn_w * 0.8)
        pauseBtn_h = round(pauseBtn_h * 0.8)

        pauseBtn_x = (self.engine.wW - window_w)/2 + ((window_w - pauseBtn_w) / 2) 

        pause_spaceBetween = ((window_h - (pauseBtn_h * 3)) / 4) - window_h * 0.1

        self.pause_resume = Button(pauseBtn_x + self.engine.wW * 0.015, (self.engine.wH - window_h)/2 + pause_spaceBetween + (window_h * 0.04)*3 + (pauseBtn_h + pause_spaceBetween)* 0, pauseBtn_h, "", main_txtsize, self.engine, self.pause_buttons, ["guiMenu", "pause", "resumeButton", "normal"])
        self.pause_menu = Button(pauseBtn_x + self.engine.wW * 0.015, (self.engine.wH - window_h)/2 + pause_spaceBetween + (window_h * 0.04)*3 + (pauseBtn_h + pause_spaceBetween)* 1, pauseBtn_h, "", main_txtsize, self.engine, self.pause_buttons, ["guiMenu", "pause", "menuButton", "normal"])
        self.pause_exit = Button(pauseBtn_x +  self.engine.wW * 0.015, (self.engine.wH - window_h)/2 + pause_spaceBetween + (window_h * 0.04)*3 + (pauseBtn_h + pause_spaceBetween)* 2, pauseBtn_h, "", main_txtsize, self.engine, self.pause_buttons, ["guiMenu", "pause", "exitButton", "normal"])


        # #----------------Option menu-------------------
        # self.option_backB = Button(self.engine.wW * 0.02, self.engine.wH * 0.02, button_w, button_h, ("menu", "option", "back_btn") , 45, self.engine,self.option_buttons)

        # self.option_frB = Button(button_x - button_w / 2, btn1_y, button_w, button_h, ("menu", "option", "fr_btn"), 45, self.engine,self.option_buttons)
        # self.option_enB = Button(button_x + button_w / 2, btn1_y, button_w, button_h, ("menu", "option", "en_btn"), 45, self.engine,self.option_buttons)
    

    #-------Main Menu fonction---------
    def main_not_hover(self):
        for x in self.main_buttons:
            x.jsonPath[3] = "normal"
            x.update()
    
    def pause_not_hover(self):
        for x in self.pause_buttons:
            x.jsonPath[3] = "normal"
            x.update()

    def main_hover(self, button):
        button.jsonPath[3] = "hover"

        #-----------Flèche hover---------
        #Left
        leftArrow_texturePath = ASSETS["guiMenu"]["allMenu"]["hoverButtonArrow"]["right"]
        leftArrow_loadTexture = pg.image.load(leftArrow_texturePath).convert_alpha()
        im = Image.open(leftArrow_texturePath)
        w,h = im.size
        ratio = w/h
        h = round(button.h * 1.5)
        w = round(h * ratio)
        leftArrow_loadTexture = pg.transform.scale(leftArrow_loadTexture, (w,h))
        rectLeftArrow = pg.Rect(button.x - w - 10, button.y - (h - button.h) / 2, w, h)
        self.engine.window.blit(leftArrow_loadTexture,rectLeftArrow)

        #Right
        rightArrow_texturePath = ASSETS["guiMenu"]["allMenu"]["hoverButtonArrow"]["left"]
        rightArrow_loadTexture = pg.image.load(rightArrow_texturePath).convert_alpha()
        rightArrow_loadTexture = pg.transform.scale(rightArrow_loadTexture, (w,h))
        rectRightArrow = pg.Rect(button.x + button.w + 10, button.y - (h - button.h) / 2, w, h)
        self.engine.window.blit(rightArrow_loadTexture,rectRightArrow)
        button.update()

    def pause_hover(self, button):
        button.jsonPath[3] = "hover"


    #-------Global Menu Fonction--------
    def txt_btn_update(self):
        for x in self.pause_buttons:
            x.text = self.engine.Dialog[x.path_txt[0]][x.path_txt[1]][x.path_txt[2]]
            x.update()
        for x in self.option_buttons:
            x.text = self.engine.Dialog[x.path_txt[0]][x.path_txt[1]][x.path_txt[2]]
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
                        self.onoff = "off"
                        

            if (self.onoff == "on"):

                if self.statut == "main":

                    self.engine.window.blit(self.main_loadBackground,self.main_backgroudRect)

                    if self.main_play.rect.collidepoint(pg.mouse.get_pos()) and event.type == pg.MOUSEBUTTONDOWN and event.button==1:
                        pass
                    
                    elif self.main_newGame.rect.collidepoint(pg.mouse.get_pos()) and event.type == pg.MOUSEBUTTONDOWN and event.button==1:
                        pass

                    elif self.main_leaderboard.rect.collidepoint(pg.mouse.get_pos()) and event.type == pg.MOUSEBUTTONDOWN and event.button==1:
                        pass

                    elif self.main_saves.rect.collidepoint(pg.mouse.get_pos()) and event.type == pg.MOUSEBUTTONDOWN and event.button==1:
                        pass

                    elif self.main_options.rect.collidepoint(pg.mouse.get_pos()) and event.type == pg.MOUSEBUTTONDOWN and event.button==1:
                        pass #self.statut = "options"

                    elif self.main_exit.rectTexture.collidepoint(pg.mouse.get_pos()) and event.type == pg.MOUSEBUTTONDOWN and event.button==1:
                        pg.quit()
                        sys.exit()

                    if event.type == pg.MOUSEMOTION:

                        self.main_not_hover()

                        if self.main_play.rectTexture.collidepoint(pg.mouse.get_pos()):
                            self.main_hover(self.main_play)
                        if self.main_newGame.rectTexture.collidepoint(pg.mouse.get_pos()):
                            self.main_hover(self.main_newGame)
                        if self.main_leaderboard.rectTexture.collidepoint(pg.mouse.get_pos()):
                            self.main_hover(self.main_leaderboard)
                        if self.main_saves.rectTexture.collidepoint(pg.mouse.get_pos()):
                            self.main_hover(self.main_saves)
                        if self.main_options.rectTexture.collidepoint(pg.mouse.get_pos()):
                            self.main_hover(self.main_options)
                        if self.main_exit.rectTexture.collidepoint(pg.mouse.get_pos()):
                            self.main_hover(self.main_exit)
                        
                        

                    
                    self.main_buttons.update()
                    self.main_buttons.draw(self.engine.window)

                elif self.statut == "pause":
                    self.engine.window.blit(self.pause_loadBgFilter,self.pause_BgFilterRect)
                    self.engine.window.blit(self.pause_loadWindow,self.pause_windowRect)

                    if event.type == pg.MOUSEMOTION:

                        self.pause_not_hover()

                        if self.pause_resume.rectTexture.collidepoint(pg.mouse.get_pos()):
                            self.pause_hover(self.pause_resume)
                        if self.pause_menu.rectTexture.collidepoint(pg.mouse.get_pos()):
                            self.pause_hover(self.pause_menu)
                        if self.pause_exit.rectTexture.collidepoint(pg.mouse.get_pos()):
                            self.pause_hover(self.pause_exit)
                        
                    
                    self.pause_buttons.update()
                    self.pause_buttons.draw(self.engine.window)
                
                # if self.statut == "options":

                #     if self.option_backB.rect.collidepoint(pg.mouse.get_pos()) and event.type == pg.MOUSEBUTTONDOWN and event.button==1:
                #         self.statut = "pause"

                #     elif self.option_frB.rect.collidepoint(pg.mouse.get_pos()) and event.type == pg.MOUSEBUTTONDOWN and event.button==1:
                #         if self.engine.Ln != "fr":
                #             self.engine.Ln = "fr"
                #             self.engine.Dialog = loadDialog("fr")
                #             self.txt_btn_update()
                            

                #     elif self.option_enB.rect.collidepoint(pg.mouse.get_pos()) and event.type == pg.MOUSEBUTTONDOWN and event.button==1:
                #         if self.engine.Ln != "en":
                #             self.engine.Ln = "en"
                #             self.engine.Dialog = loadDialog("en")
                #             self.txt_btn_update()


                    
                #     if event.type == pg.MOUSEMOTION:

                #         if self.option_backB.rect.collidepoint(pg.mouse.get_pos()):
                #             self.hover()
                #         elif self.option_frB.rect.collidepoint(pg.mouse.get_pos()):
                #             self.hover()
                #         elif self.option_enB.rect.collidepoint(pg.mouse.get_pos()):
                #             self.hover()

                #         else:
                #             self.not_hover()

                #     self.option_buttons.update()
                #     self.option_buttons.draw(self.engine.window)


                
                    
                    
                        









                

        
        

