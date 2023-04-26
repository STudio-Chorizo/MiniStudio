import pygame as pg
import sys
from PIL import Image
from dependencies.engine.gameobject import *
from dependencies.parsejson.parse import *
from dependencies.music.music_control import Playlist

main_buttons = pg.sprite.Group()
pause_buttons = pg.sprite.Group()
options_buttons = pg.sprite.Group()
optionsText = pg.sprite.Group()

class Button(pg.sprite.Sprite):
            def __init__(self, x, y, h, path_txt, txtSize, Engine, list, jsonPath, id):
                super().__init__()

                self.engine = Engine

                self.id = id

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
                
                self.update()
                list.add(self)

                

            def update(self):
                if self.path_txt != "":
                    self.text = self.engine.Dialog[self.path_txt[0]][self.path_txt[1]][self.path_txt[2]]
                else :
                    self.text = ""
                self.texturePath = ASSETS[self.jsonPath[0]][self.jsonPath[1]][self.jsonPath[2]][self.jsonPath[3]]
                self.loadTexture = pg.image.load(self.texturePath).convert_alpha()
                self.loadTexture = pg.transform.scale(self.loadTexture, (self.w,self.h))
                self.font = pg.font.Font("Assets/font/Orbitron-Black.ttf", self.txtSize)
                self.text_render = self.font.render(self.text, 1, "white")
                self.image = self.text_render
                self.txt_x, self.txt_y, self.txt_w , self.txt_h = self.text_render.get_rect()
                self.rect = pg.Rect(self.x + (self.w - self.txt_w) / 2, self.y + (self.h - self.txt_h) / 2, self.w, self.h)
                self.rectTexture = pg.Rect(self.x, self.y, self.w, self.h)
                self.engine.surface.blit(self.loadTexture,self.rectTexture)

class Text(pg.sprite.Sprite):
            def __init__(self, x, y, w, h, path_txt, txtSize, Engine, list):
                super().__init__()

                self.engine = Engine

                self.x = x
                self.y = y
                self.w = w
                self.h = h
                self.path_txt = path_txt
                self.text = self.engine.Dialog[self.path_txt[0]][self.path_txt[1]][self.path_txt[2]]

                self.txtSize = txtSize
                self.colors = "black"
                self.font = pg.font.Font("Assets/font/Orbitron-Black.ttf", self.txtSize)
                self.text_render = self.font.render(self.text, 1, "white")
                self.image = self.text_render
                self.txt_x, self.txt_y, self.txt_w , self.txt_h = self.text_render.get_rect()

                self.rect = pg.Rect(self.x + (self.w - self.txt_w) / 2, self.y + (self.h - self.txt_h) / 2, self.w, self.h)
                
                self.update()
                list.add(self)

            def update(self):
                self.text = self.engine.Dialog[self.path_txt[0]][self.path_txt[1]][self.path_txt[2]]
                self.font = pg.font.Font("Assets/font/Orbitron-Black.ttf", self.txtSize)
                self.text_render = self.font.render(self.text, 1, "white")
                self.image = self.text_render
                self.txt_x, self.txt_y, self.txt_w , self.txt_h = self.text_render.get_rect()
                self.rect = pg.Rect(self.x + (self.w - self.txt_w) / 2, self.y + (self.h - self.txt_h) / 2, self.w, self.h)
                


class Menu:

    def __init__(self, engine):

        self.onoff = "on"
        self.statut = "main"
        self.engine = engine
        self.window = engine.window

        self.main_buttons = main_buttons
        self.pause_buttons = pause_buttons
        self.options_buttons = options_buttons
        self.optionsText = optionsText

        #----------------Main menu-------------------
        Playlist.Instance.miscs["menu"].play(2**15)

        self.backgroundPath = ASSETS["guiMenu"]["main"]["background"]
        self.loadBackground = pg.image.load(self.backgroundPath).convert_alpha()
        self.main_backgroudRect = pg.Rect(0, 0, self.engine.wW, self.engine.wH)
        self.main_loadBackground = pg.transform.scale(self.loadBackground, (self.engine.wW,self.engine.wH))
        self.engine.surface.blit(self.main_loadBackground,self.main_backgroudRect)

        main_topmarge = 0.24
        
        main_button_x = self.engine.wW * 0.05
        main_button_h = self.engine.wH * 0.05
        main_txtsize = 25
        main_spaceBetween = ((self.engine.wH - self.engine.wH * main_topmarge) - (main_button_h * 6)) / 7
        
        self.engine.wH * main_topmarge + main_spaceBetween + (main_button_h + main_spaceBetween)* 0

        self.main_play = Button(main_button_x, self.engine.wH * main_topmarge + main_spaceBetween + (main_button_h + main_spaceBetween)* 0, main_button_h, ("menu", "main", "play_btn"), main_txtsize, self.engine, self.main_buttons, ["guiMenu", "main", "playButton", "normal"],0)
        self.main_newGame = Button(main_button_x, self.engine.wH * main_topmarge + main_spaceBetween + (main_button_h + main_spaceBetween)* 1, main_button_h, ("menu", "main", "newGame_btn"), main_txtsize, self.engine, self.main_buttons, ["guiMenu", "main", "newGameButton", "normal"],1)
        self.main_leaderboard = Button(main_button_x, self.engine.wH * main_topmarge + main_spaceBetween + (main_button_h + main_spaceBetween)* 2, main_button_h, ("menu", "main", "leaderboard_btn"), main_txtsize, self.engine, self.main_buttons, ["guiMenu", "main", "leaderboardButton", "normal"],2)
        self.main_saves = Button(main_button_x, self.engine.wH * main_topmarge + main_spaceBetween + (main_button_h + main_spaceBetween)* 3, main_button_h, ("menu", "main", "saves_btn"), main_txtsize, self.engine, self.main_buttons, ["guiMenu", "main", "savesButton", "normal"],3)
        self.main_options = Button(main_button_x, self.engine.wH * main_topmarge + main_spaceBetween + (main_button_h + main_spaceBetween)* 4, main_button_h, ("menu", "main", "options_btn"), main_txtsize, self.engine, self.main_buttons, ["guiMenu", "main", "optionsButton", "normal"],4)
        self.main_exit = Button(main_button_x, self.engine.wH * main_topmarge + main_spaceBetween + (main_button_h + main_spaceBetween)* 5, main_button_h, ("menu", "main", "exit_btn"), main_txtsize, self.engine, self.main_buttons, ["guiMenu", "main", "exitButton", "normal"],5)

        #----------------Pause menu-------------------
        #Background Filter
        self.pause_BgFilterPath = ASSETS["guiMenu"]["allMenu"]["backgroundFilter"]
        self.pause_loadBgFilter = pg.image.load(self.pause_BgFilterPath).convert_alpha()
        self.pause_BgFilterRect = pg.Rect(0, 0, self.engine.wW, self.engine.wH)
        self.pause_loadBgFilter = pg.transform.scale(self.pause_loadBgFilter, (self.engine.wW,self.engine.wH))
        self.engine.surface.blit(self.pause_loadBgFilter,self.pause_BgFilterRect)

        #Window skin
        self.pause_windowPath = ASSETS["guiMenu"]["allMenu"]["window"]
        self.pause_loadWindow = pg.image.load(self.pause_windowPath).convert_alpha()
        pause_window = Image.open(self.pause_windowPath)
        window_w, window_h = pause_window.size
        self.pause_windowRect = pg.Rect((self.engine.wW - window_w)/2, (self.engine.wH - window_h)/2, window_w, window_h)
        self.pause_loadWindow = pg.transform.scale(self.pause_loadWindow, (window_w, window_h))
        self.engine.surface.blit(self.pause_loadWindow,self.pause_windowRect)

        #Buttons
        pauseBtn = Image.open(ASSETS["guiMenu"]["pause"]["resumeButton"]["normal"])
        pauseBtn_w, pauseBtn_h = pauseBtn.size
        pauseBtn_w = round(pauseBtn_w * 0.8)
        pauseBtn_h = round(pauseBtn_h * 0.8)

        pauseBtn_x = (self.engine.wW - window_w)/2 + ((window_w - pauseBtn_w) / 2) 

        pause_spaceBetween = ((window_h - (pauseBtn_h * 3)) / 4) - window_h * 0.1

        self.pause_resume = Button(pauseBtn_x + self.engine.wW * 0.015, (self.engine.wH - window_h)/2 + pause_spaceBetween + (window_h * 0.075)*3 + (pauseBtn_h + pause_spaceBetween)* 0, pauseBtn_h, "", main_txtsize, self.engine, self.pause_buttons, ["guiMenu", "pause", "resumeButton", "normal"],0)
        self.pause_menu = Button(pauseBtn_x + self.engine.wW * 0.015, (self.engine.wH - window_h)/2 + pause_spaceBetween + (window_h * 0.075)*3 + (pauseBtn_h + pause_spaceBetween)* 1, pauseBtn_h, "", main_txtsize, self.engine, self.pause_buttons, ["guiMenu", "pause", "menuButton", "normal"],1)
        self.pause_exit = Button(pauseBtn_x +  self.engine.wW * 0.015, (self.engine.wH - window_h)/2 + pause_spaceBetween + (window_h * 0.075)*3 + (pauseBtn_h + pause_spaceBetween)* 2, pauseBtn_h, "", main_txtsize, self.engine, self.pause_buttons, ["guiMenu", "pause", "exitButton", "normal"],2)

        #----------------options menu-------------------
        #Background Filter
        self.options_BgFilterPath = ASSETS["guiMenu"]["allMenu"]["backgroundFilter"]
        self.options_loadBgFilter = pg.image.load(self.options_BgFilterPath).convert_alpha()
        self.options_BgFilterRect = pg.Rect(0, 0, self.engine.wW, self.engine.wH)
        self.options_loadBgFilter = pg.transform.scale(self.options_loadBgFilter, (self.engine.wW,self.engine.wH))
        self.engine.surface.blit(self.options_loadBgFilter,self.options_BgFilterRect)

        #Window skin
        self.options_windowPath = ASSETS["guiMenu"]["allMenu"]["window"]
        self.options_loadWindow = pg.image.load(self.options_windowPath).convert_alpha()
        options_window = Image.open(self.options_windowPath)
        window_w, window_h = options_window.size
        self.options_windowRect = pg.Rect((self.engine.wW - window_w)/2, (self.engine.wH - window_h)/2, window_w, window_h)
        self.options_loadWindow = pg.transform.scale(self.options_loadWindow, (window_w, window_h))
        self.engine.surface.blit(self.options_loadWindow,self.options_windowRect)


        optionsTitle_w = window_w * 0.75
        optionsTitle_h = window_h * 0.1
        optionsTitle_x = (self.engine.wW - window_w)/2 + (window_w - optionsTitle_w)/2
        optionsTitle_y = (self.engine.wH - window_h)/2 + (self.engine.wH * 0.15)

        self.optionsTitle = Text(optionsTitle_x, optionsTitle_y, optionsTitle_w, optionsTitle_h, ("menu", "options", "title"), 45, self.engine, self.optionsText)

        optionsLangTxt_x = (self.engine.wW - window_w)/2 + window_w * 0.1
        optionsLangTxt_y = optionsTitle_y + optionsTitle_h * 1.5
        self.optionsLangTxt = Text(optionsLangTxt_x, optionsLangTxt_y, window_w * 0.5, optionsTitle_h, ("menu", "options", "lang"), 45, self.engine, self.optionsText)

        self.optionsLangBtn = Button(optionsLangTxt_x + window_w * 0.45, optionsLangTxt_y + (optionsTitle_h - window_h * 0.05)/2, window_h * 0.05, ("menu", "options", "langSelect"), main_txtsize, self.engine, self.options_buttons, ["guiMenu", "main", "playButton", "normal"],0)
        self.optionsBackBtn = Button((self.engine.wW - window_w)/2 + (self.engine.wW * 0.2), (self.engine.wH - window_h)/2 + window_h - (self.engine.wH * 0.15), window_h * 0.05, ("menu", "options", "back"), main_txtsize, self.engine, self.options_buttons, ["guiMenu", "main", "exitButton", "normal"],1)


        #----------------Quest menu-------------------
        #Background
        self.quest_BackgroundPath = ASSETS["guiMenu"]["quest"]["demo"]
        self.quest_loadBackground = pg.image.load(self.quest_BackgroundPath).convert_alpha()
        self.quest_BackgroundRect = pg.Rect(0, 0, self.engine.wW, self.engine.wH)
        self.quest_loadBackground = pg.transform.scale(self.quest_loadBackground, (self.engine.wW,self.engine.wH))


        #key
        self.keyDown = False
        self.keyPressed = ""
        self.buttonPressed = ""


        self.selected = 0
    

    #-------Menu fonction---------
    def main_not_hover(self, button):
        button.jsonPath[3] = "normal"
        button.update()
    
    def pause_not_hover(self, button):
        button.jsonPath[3] = "normal"
        button.update()

    def options_not_hover(self, button):
        button.jsonPath[3] = "normal"
        button.update()

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
        self.engine.surface.blit(leftArrow_loadTexture,rectLeftArrow)

        #Right
        rightArrow_texturePath = ASSETS["guiMenu"]["allMenu"]["hoverButtonArrow"]["left"]
        rightArrow_loadTexture = pg.image.load(rightArrow_texturePath).convert_alpha()
        rightArrow_loadTexture = pg.transform.scale(rightArrow_loadTexture, (w,h))
        rectRightArrow = pg.Rect(button.x + button.w + 10, button.y - (h - button.h) / 2, w, h)
        self.engine.surface.blit(rightArrow_loadTexture,rectRightArrow)
        button.update()

    def pause_hover(self, button):
        button.jsonPath[3] = "hover"

    def options_hover(self, button):
        button.jsonPath[3] = "hover"


    #-------Global Menu Fonction--------
    
    def switchOn(self):
        if self.onoff == "off":
            Playlist.Instance.miscs["menu"].set_volume(0)
        Playlist.Instance.miscs["menu"].smooth_volume(100)
        Playlist.Instance.miscs["menu"].play(2**15)
        Playlist.Instance.miscs["game"].smooth_volume(0)

        self.onoff = "on"
        self.engine.speedTime = 0.0

        pg.event.set_grab(False)
        pg.mouse.set_visible(True)
    
    def switchOff(self):
        if self.onoff == "on":
            Playlist.Instance.miscs["game"].set_volume(0)
        Playlist.Instance.miscs["game"].smooth_volume(100)
        Playlist.Instance.miscs["game"].play(2**15)
        Playlist.Instance.miscs["menu"].smooth_volume(0)

        self.onoff = "off"
        self.engine.speedTime = 1.0

        pg.event.set_grab(True)
        pg.mouse.set_visible(False)
    
    def switchOnOff(self):
        if self.onoff == "off":
            self.switchOn()
        elif self.onoff == "on":
            self.switchOff()

    def Update(self):

        keys = pg.key.get_pressed()
        mouse = pg.mouse.get_pressed()
        mousePos = pg.mouse.get_pos()

        if (keys[pg.K_ESCAPE] or self.engine.joystick.get_button(7)) and self.keyDown == False and self.statut == "pause":
            self.switchOnOff()
            self.keyDown = True
            self.keyPressed = "Escape"
        elif not (keys[pg.K_ESCAPE] or self.engine.joystick.get_button(7)) and self.keyDown == True and self.keyPressed == "Escape" and self.statut == "pause":
            self.keyDown = False

        if (self.onoff == "on"):

            if self.statut == "main":

                self.engine.surface.blit(self.main_loadBackground,self.main_backgroudRect)

                if (self.main_play.rect.collidepoint(mousePos) and mouse[0] and self.keyDown == False) or (self.selected == self.main_play.id and self.engine.joystick.get_button(0) and self.keyDown == False):
                    self.switchOnOff()
                    self.statut = "pause"

                elif (self.main_leaderboard.rect.collidepoint(mousePos) and mouse[0] and self.keyDown == False) or (self.selected == self.main_leaderboard.id and self.engine.joystick.get_button(0) and self.keyDown == False):
                    self.statut = "quest"
                    self.keyDown == True
                    self.keyPressed == "main_leaderboard"
                elif not mouse[0] and not self.engine.joystick.get_button(0) and self.keyDown == True and self.keyPressed == "main_leaderboard":
                    self.keyDown = False

                elif (self.main_options.rect.collidepoint(mousePos) and mouse[0] and self.keyDown == False) or (self.selected == self.main_options.id and self.engine.joystick.get_button(0) and self.keyDown == False):
                    self.statut = "options"
                    self.keyDown == True
                    self.keyPressed == "main_options"
                elif not mouse[0] and not self.engine.joystick.get_button(0) and self.keyDown == True and self.keyPressed == "main_options":
                    self.keyDown = False

                elif (self.main_exit.rect.collidepoint(mousePos) and mouse[0] and self.keyDown == False) or (self.selected == self.main_exit.id and self.engine.joystick.get_button(0) and self.keyDown == False):
                    self.engine.run = False

                elif (mouse[0] or self.engine.joystick.get_button(0)) and self.keyDown == False:
                    self.keyDown = True
                    self.keyPressed = "debug"
                elif (not mouse[0] or not self.engine.joystick.get_button(0)) and self.keyDown == True and self.keyPressed == "debug":
                    self.keyDown = False

                if self.engine.joystick.get_axis(1) < -0.1 and self.keyDown == False:
                    self.selected = (self.selected - 1) % 6
                    self.keyDown = True
                    self.keyPressed = "z"
                elif not self.engine.joystick.get_axis(1) < -0.1 and self.keyDown == True and self.keyPressed == "z":
                    self.keyDown = False
                elif self.engine.joystick.get_axis(1) > 0.1 and self.keyDown == False:
                    self.selected = (self.selected + 1) % 6
                    self.keyDown = True
                    self.keyPressed = "s"
                elif not self.engine.joystick.get_axis(1) > 0.1 and self.keyDown == True and self.keyPressed == "s":
                    self.keyDown = False

                if self.main_play.rectTexture.collidepoint(mousePos):
                    self.selected = 0
                if self.main_newGame.rectTexture.collidepoint(mousePos):
                    self.selected = 1
                if self.main_leaderboard.rectTexture.collidepoint(mousePos):
                    self.selected = 2
                if self.main_saves.rectTexture.collidepoint(mousePos):
                    self.selected = 3
                if self.main_options.rectTexture.collidepoint(mousePos):
                    self.selected = 4
                if self.main_exit.rectTexture.collidepoint(mousePos):
                    self.selected = 5
                
                for x in main_buttons:
                    if x.id == self.selected:
                        self.main_hover(x)
                    else : self.main_not_hover(x)
                
                self.main_buttons.update()
                self.main_buttons.draw(self.engine.surface)

            elif self.statut == "pause":
                self.engine.surface.blit(self.pause_loadBgFilter,self.pause_BgFilterRect)
                self.engine.surface.blit(self.pause_loadWindow,self.pause_windowRect)

                if (self.pause_resume.rectTexture.collidepoint(mousePos) and mouse[0]) or (self.selected == self.pause_resume.id and self.engine.joystick.get_button(0)) or (self.engine.joystick.get_button(1) and self.keyDown == False):
                    self.switchOnOff()
                    self.keyPressed == "pause_resume"

                elif (self.pause_menu.rectTexture.collidepoint(mousePos) and mouse[0]) or (self.selected == self.pause_menu.id and self.engine.joystick.get_button(0) and self.keyDown == False):
                    self.statut = "quest"
                    self.keyDown == True
                    self.keyPressed == "pause_menu"
                elif not mouse[0] and not self.engine.joystick.get_button(0) and self.keyDown == True and self.keyPressed == "pause_menu":
                    self.keyDown = False

                elif (self.pause_exit.rectTexture.collidepoint(mousePos) and mouse[0]) or (self.selected == self.pause_exit.id and self.engine.joystick.get_button(0) and self.keyDown == False):
                    self.selected = 9
                    self.statut = "main"
                    self.keyDown == True
                    self.keyPressed == "pause_exit"
                elif not mouse[0] and not self.engine.joystick.get_button(0) and self.keyDown == True and self.keyPressed == "pause_exit":
                    self.keyDown = False

                if self.engine.joystick.get_axis(1) < -0.1 and self.keyDown == False:
                    self.selected = (self.selected - 1) % 3
                    self.keyDown = True
                    self.keyPressed = "z"
                elif not self.engine.joystick.get_axis(1) < -0.1 and self.keyDown == True and self.keyPressed == "z":
                    self.keyDown = False
                elif self.engine.joystick.get_axis(1) > 0.1 and self.keyDown == False:
                    self.selected = (self.selected + 1) % 3
                    self.keyDown = True
                    self.keyPressed = "s"
                elif not self.engine.joystick.get_axis(1) > 0.1 and self.keyDown == True and self.keyPressed == "s":
                    self.keyDown = False

                elif (mouse[0] or self.engine.joystick.get_button(0)) and self.keyDown == False:
                    self.keyDown = True
                    self.keyPressed = "debug"
                elif (not mouse[0] or not self.engine.joystick.get_button(0)) and self.keyDown == True and self.keyPressed == "debug":
                    self.keyDown = False

                if self.pause_resume.rectTexture.collidepoint(mousePos):
                    self.selected = 0
                if self.pause_menu.rectTexture.collidepoint(mousePos):
                    self.selected = 1
                if self.pause_exit.rectTexture.collidepoint(mousePos):
                    self.selected = 2
                
                for x in pause_buttons:
                    if x.id == self.selected:
                        self.pause_hover(x)
                    else : self.pause_not_hover(x)
                    
                self.pause_buttons.update()
                self.pause_buttons.draw(self.engine.surface)
            
            elif self.statut == "options":

                self.engine.surface.blit(self.options_loadBgFilter,self.options_BgFilterRect)
                self.engine.surface.blit(self.options_loadWindow,self.options_windowRect)

                if (self.optionsLangBtn.rectTexture.collidepoint(mousePos) and mouse[0] and self.keyDown == False) or (self.selected == self.optionsLangBtn.id and self.engine.joystick.get_button(0) and self.keyDown == False):
                    self.keyPressed = "ClickLang"
                    self.engine.selectLang = (self.engine.selectLang + 1) % 2
                    self.engine.Dialog = loadDialog(self.engine.allLangs[self.engine.selectLang])
                    self.keyDown = True
                elif not mouse[0] and not self.engine.joystick.get_button(0) and self.keyDown == True and self.keyPressed == "ClickLang":
                    self.keyDown = False

                if (self.optionsBackBtn.rect.collidepoint(mousePos) and mouse[0] and self.keyDown == False) or (self.selected == self.optionsBackBtn.id and self.engine.joystick.get_button(0) and self.keyDown == False) or (self.engine.joystick.get_button(1) and self.keyDown == False):
                    self.statut = "main"

                if self.engine.joystick.get_axis(1) < -0.1 and self.keyDown == False:
                    self.selected = (self.selected - 1) % 2
                    self.keyDown = True
                    self.keyPressed = "z"
                elif not self.engine.joystick.get_axis(1) < -0.1 and self.keyDown == True and self.keyPressed == "z":
                    self.keyDown = False
                elif self.engine.joystick.get_axis(1) > 0.1 and self.keyDown == False:
                    self.selected = (self.selected + 1) % 2
                    self.keyDown = True
                    self.keyPressed = "s"
                elif not self.engine.joystick.get_axis(1) > 0.1 and self.keyDown == True and self.keyPressed == "s":
                    self.keyDown = False

                elif (mouse[0] or self.engine.joystick.get_button(0)) and self.keyDown == False:
                    self.keyDown = True
                    self.keyPressed = "debug"
                elif (not mouse[0] or not self.engine.joystick.get_button(0)) and self.keyDown == True and self.keyPressed == "debug":
                    self.keyDown = False

                if self.optionsLangBtn.rectTexture.collidepoint(mousePos):
                    self.selected = 0
                if self.optionsBackBtn.rectTexture.collidepoint(mousePos):
                    self.selected = 1
                
                for x in options_buttons:
                    if x.id == self.selected:
                        self.options_hover(x)
                    else : self.options_not_hover(x)
                
                self.options_buttons.update()
                self.options_buttons.draw(self.engine.surface)
                self.optionsText.update()
                self.optionsText.draw(self.engine.surface)


            elif self.statut == "quest":

                self.engine.surface.blit(self.quest_loadBackground,self.quest_BackgroundRect)

                if keys[pg.K_ESCAPE] or self.engine.joystick.get_button(1):
                    self.statut = "main"
                
                