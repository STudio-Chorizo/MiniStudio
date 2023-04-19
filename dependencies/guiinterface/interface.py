import time
import pygame
import dependencies.engine.engine as eng

class Guiplayer():
	def __init__(self):
		self.life = 3
		self.mun = 14

	def PlayerInfo(self):
		white = (255, 255, 255)
		Ww = 1600
		Hh = 900	
		Hr = 150
		Wrp = Ww*0.05
		Hrp = Hh*0.95 - Hr
		Wt = Ww * 0.95
		Ht = Hh * 0.95
		if self.life == 3:
			cube1 = pygame.rect.Rect(Wrp, Hrp, 50, Hr)
			cube2 = pygame.rect.Rect(Wrp+60, Hrp, 50, 150)
			cube3 = pygame.rect.Rect(Wrp+120, Hrp, 50, 150)
			pygame.draw.rect(eng.Engine.Instance.window,(0,255,0),cube1)
			pygame.draw.rect(eng.Engine.Instance.window,(0,255,0),cube2)
			pygame.draw.rect(eng.Engine.Instance.window,(0,255,0),cube3)
		elif self.life == 2:
			cube1 = pygame.rect.Rect(Wrp, Hrp, 50, Hr)
			cube2 = pygame.rect.Rect(Wrp+60, Hrp, 50, 150)
			pygame.draw.rect(eng.Engine.Instance.window,(0,255,0),cube1)
			pygame.draw.rect(eng.Engine.Instance.window,(0,255,0),cube2)
		elif self.life == 1:
			cube1 = pygame.rect.Rect(Wrp, Hrp, 50, Hr)
			pygame.draw.rect(eng.Engine.Instance.window,(0,255,0),cube1)
		elif self.life == 0:
			pass

		arial_font = pygame.font.SysFont("arial", 50)
		hello_text_surface = arial_font.render(self.mun.__str__(),True,white)
		eng.Engine.Instance.window.blit(hello_text_surface,(Wt-50, Ht - 50))
		
		pygame.display.flip()
		time.sleep(5)