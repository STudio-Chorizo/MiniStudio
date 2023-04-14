import pygame as pg
from Engine.GameObject import GameObject
from Engine.Engine import Engine

buttons = pg.sprite.Group()

class Button(pg.sprite.Sprite):
            def __init__(self, w, h, y, text, size, Engine, list):
                super().__init__()
                self.engine = Engine
                self.colors = "white"
                self.font = pg.font.SysFont("Arial", size)
                self.text_render = self.font.render(text, 1, "black")
                self.image = self.text_render
                self.txt_w , self.txt_h = self.text_render.get_rect()

                self.w = w
                self.h = h

                self.x = (self.engine.wW - self.w) / 2
                self.y = y
                self.txt_x = self.x + (self.w - self.txt_w) / 2
                self.txt_y = self.y + (self.h - self.txt_h) / 2
                
                self.rect = pg.Rect(self.x, self.y, self.w, self.h)
                self.update()
                list.add(self)

            def update(self):
                pg.draw.rect(self.engine.window, self.colors, (self.x -10, self.y - 10, self.w + 20, self.h + 20),5)



class Menu(GameObject):

    def __init__(self, engine, position = [0, 0, 0], rot = [0, 0, 0], scale = [0, 0, 0]):
        super().__init__(position,rot,scale)

        self.statut = "on"
        self.engine = engine
        self.window = engine.window

        #Surface data
        marge = 0.04
        self.surface_w = engine.wW - (engine.wW * marge * 2)
        self.surface_h = engine.wH - (engine.wH * marge * 2)
        self.surface_x = engine.wW * marge
        self.surface_y = engine.wH * marge
        
        self.buttons = buttons

        self.surface = pg.draw.rect(self.window,(255,255,255),[self.surface_x, self.surface_y, self.surface_w,self.surface_h])

        button_h = 120
        button_w = 300

        spaceBetween = (self.engine.wH - button_h * 3) / 4
        self.btn1_y = spaceBetween
        self.btn2_y = spaceBetween + 1 * (button_w + spaceBetween)
        self.btn3_y = spaceBetween + 2 * (button_w + spaceBetween)
        
        self.b0 = Button(button_w, button_h, self.btn1_y , "Resume", 55, self.engine,self.buttons)
        self.b1 = Button(button_w, button_h, self.btn2_y , "Resume", 55, self.engine,self.buttons)
        self.b2 = Button(button_w, button_h, self.btn3_y , "Resume", 55, self.engine,self.buttons)

    def not_hover(self):
        for x in self.buttons:
            x.colors = "black"
            x.update()



    def Update(self):
        for event in pg.event.get():
            if (event.type == pg.QUIT):
                pg.quit()

            if (event.type == pg.K_ESCAPE):
                self.statut = "on"

            if (self.statut == "on"):

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

        
        

