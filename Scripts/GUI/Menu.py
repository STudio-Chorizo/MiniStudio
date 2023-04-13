import pygame as pg
from Engine.GameObject import GameObject
from Engine.Engine import Engine



class Menu(GameObject):

    def __init__(self, engine, position = [0, 0, 0], rot = [0, 0, 0], scale = [0, 0, 0]):
        super().__init__(position,rot,scale)

        self.window = engine.window

        #Surface data
        marge = 0.04
        self.surface_w = engine.wW - (engine.wW * marge * 2)
        self.surface_h = engine.wH - (engine.wH * marge * 2)
        self.surface_x = engine.wW * marge
        self.surface_y = engine.wH * marge

        #Button data
        self.btn_w = engine.wW * 0.15
        self.btn_h = engine.wH * 0.1
        self.btn_x = (engine.wW - self.btn_w) / 2

        spaceBetween = (engine.wH - self.btn_h * 3) / 4

        self.btn1_y = spaceBetween
        self.btn2_y = spaceBetween + 1 * (self.btn_h + spaceBetween)
        self.btn3_y = spaceBetween + 2 * (self.btn_h + spaceBetween)

        self.btn_rgb_nohover = [170,170,170,0.8]
        self.btn_rgb_hover = [0,0,0]

        self.btn1_actual_rgb = [170,170,170,0.8]
        self.btn2_actual_rgb = [170,170,170,0.8]
        self.btn3_actual_rgb = [170,170,170,0.8]
        

        # buttons = pg.sprite.Group()
        # class Button(Menu):
        #     def __init__(self, screen, position, text, size, colors="white"):
        #         self.window = screen
        #         self.colors = colors
        #         self.font = pg.font.SysFont("Arial", size)
        #         self.text_render = self.font.render(text, 1, "white")
        #         self.image = self.text_render
        #         self.x, self.y, self.w , self.h = self.text_render.get_rect()
        #         self.x, self.y = position
        #         self.rect = pg.Rect(self.x, self.y, self.w, self.h)
        #         self.position = position
        #         self.update()


        #     def update(self):
        #         pg.draw.rect(engine.window, self.colors, (self.x, self.y, self.w , self.h),4)


        # b0 = Button(engine.window, (15, 15), "test", 70, "black")

        

        






    def Update(self, Engine):
        
        self.surface = pg.draw.rect(self.window,(255,255,255),[self.surface_x, self.surface_y, self.surface_w,self.surface_h])

        self.btn1 = pg.draw.rect(self.window,(self.btn1_actual_rgb),[self.btn_x, self.btn1_y, self.btn_w,self.btn_h],3)

        self.btn2 = pg.draw.rect(self.window,(self.btn2_actual_rgb),[self.btn_x, self.btn2_y , self.btn_w,self.btn_h],3)

        self.btn3 = pg.draw.rect(self.window,(self.btn3_actual_rgb),[self.btn_x, self.btn3_y, self.btn_w,self.btn_h],3)



        for event in pg.event.get():
            if event.type == pg.MOUSEMOTION:
                if self.btn1.collidepoint(pg.mouse.get_pos()):
                    self.btn1_actual_rgb = self.btn_rgb_hover
                else : self.btn1_actual_rgb = self.btn_rgb_nohover

                if self.btn2.collidepoint(pg.mouse.get_pos()):
                    self.btn2_actual_rgb = self.btn_rgb_hover
                    
                else : self.btn2_actual_rgb = self.btn_rgb_nohover

                if self.btn3.collidepoint(pg.mouse.get_pos()):
                    self.btn3_actual_rgb = self.btn_rgb_hover
                else : self.btn3_actual_rgb = self.btn_rgb_nohover

