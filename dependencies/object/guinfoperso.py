import time
from tkinter import TRUE
import pygame

class Guiplayer:
	def __init__(self):
		self.life = 3
		self.mun = 14

	def LifePlayer(self):
		white = (255, 255, 255)
		bleu = (0, 0, 128)
		pygame.init()
		pygame.init()
		Ww = 1600
		Hh = 900	
		Hr = 150
		Wrp = Ww*0.05
		Hrp = Hh*0.95 - Hr
		Wt = Ww * 0.95
		Ht = Hh * 0.95
		window = pygame.display.set_mode((Ww, Hh))
		pygame.display.set_caption(("waiting"))
		if self.life == 3:
			cube1 = pygame.rect.Rect(Wrp, Hrp, 50, Hr)
			cube2 = pygame.rect.Rect(Wrp+60, Hrp, 50, 150)
			cube3 = pygame.rect.Rect(Wrp+120, Hrp, 50, 150)
			pygame.draw.rect(window,(0,255,0),cube1)
			pygame.draw.rect(window,(0,255,0),cube2)
			pygame.draw.rect(window,(0,255,0),cube3)
		elif self.life == 2:
			cube1 = pygame.rect.Rect(Wrp, Hrp, 50, Hr)
			cube2 = pygame.rect.Rect(Wrp+60, Hrp, 50, 150)
			pygame.draw.rect(window,(0,255,0),cube1)
			pygame.draw.rect(window,(0,255,0),cube2)
		elif self.life == 1:
			cube1 = pygame.rect.Rect(Wrp, Hrp, 50, Hr)
			pygame.draw.rect(window,(0,255,0),cube1)
		elif self.life == 0:
			pass

		arial_font = pygame.font.SysFont("arial", 50)
		hello_text_surface = arial_font.render(self.mun.__str__(),True,white)
		window.blit(hello_text_surface,(Wt-50, Ht - 50))
		
		pygame.display.flip()
		time.sleep(5)
		