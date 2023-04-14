
import pygame

pygame.init()
screen = pygame.display.set_mode((600, 400))
screen.fill("black")

buttons = pygame.sprite.Group()
class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, text, size):
        super().__init__()
        self.colors = "white"
        self.font = pygame.font.SysFont("Arial", size)
        self.text_render = self.font.render(text, 1, "white")
        self.image = self.text_render
        self.x, self.y, self.w , self.h = self.text_render.get_rect()
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        self.position = [x,y]
        self.update()
        buttons.add(self)

    def update(self):
        pygame.draw.rect(screen, self.colors, (self.x -10, self.y - 10, self.w + 20, self.h + 20),5)
        # screen.blit(self.text_render, self.position)

        # self.rect = screen, position, text, size, colors="white on blue"screen.blit(self.text_render, (self.x, self.y))



def not_hover():
    for x in buttons:
        x.colors = "black"
        x.update()


b0 = Button(10,10 , "Resume", 55)
b1 = Button(10,210, "Option", 55)
b2 = Button(10,410, "Exit", 55)

while True:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
            if event.type == pygame.MOUSEMOTION:
                # 2. put the collide check for mouse hover here for each button
                if b0.rect.collidepoint(pygame.mouse.get_pos()):
                    b0.colors = "white"
                elif b1.rect.collidepoint(pygame.mouse.get_pos()):
                    b1.colors = "white"
                elif b2.rect.collidepoint(pygame.mouse.get_pos()):
                    b2.colors = "white"
                else:
                    # this will work for every buttons going back to original color after mouse goes out
                    not_hover()
                    
        buttons.update()
        buttons.draw(screen)
        pygame.display.update()
