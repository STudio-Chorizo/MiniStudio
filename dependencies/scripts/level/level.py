
import json
import time
import pygame


class Level:
    def __init__(self):
        self.Ln = 0
    
    def LoadNiveau(self,Ln):
        white = (255,255,255)
        window = pygame.display.set_mode((800, 666))
        pygame.display.set_caption(("waiting"))
        time.sleep(1)
        self.Ln = Ln
        #faut rajouter l'argument si dessou qui est l'emplacement des asset
        self.data = json.loads()
        return self.data[Ln]
    
