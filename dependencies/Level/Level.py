
import time
import pygame


class Level:
    def __init__(self):
        self.Ln = 0
    
    def LoadNiveau(self,Ln):
        white = (255,255,255)
        window = pygame.display.set_mode((800, 666))
        pygame.display.set_caption(("Dinosaur - waiting"))
        time.sleep(1)
        run = True
        while run:
            self.Ln = Ln
            self.data = json.loads()
            return self.data[Ln]
            run = False
    
