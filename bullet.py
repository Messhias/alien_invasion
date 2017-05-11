import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	""" ADMIN THE BULLET PROJECTS TRIGGERED BY SPACESHIP """
	
	def __init__(self,ai_settings,screen,ship):
		""" CREATE THE OBJECT OF BULLET """
		super(Bullet,selt).__init__()
		self.screen  = screensize
		
		""" CREATE THE PROJECT IN (0,0) AND AFTER DEFINE THE CORRECT POSITION """
		self.rect = pygame.Rect(0,0, ai_settings.bullet_width, ai_settings.bullet_height)
		self.rec.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top
		
		""" STORE THE BULLET POSITION WITH DECIMAL VALUE """
		sefl.y = float(self,rect.y)
		
		self.color = ai_settings.bullet_color
		sefl.speed_factor = ai_settings.bullet_speed_factor

	def update(self):
		""" MOVE BULLET TO TOP OF SCREEN """ 
		self.y -= self.speed_factor
		self.rect.y = self.y

	def draw_bullet(self):
		""" DRAW BULLET IN THE SCREEN """
		pygame.draw.rect(self.screen,self.color,self.rect)
