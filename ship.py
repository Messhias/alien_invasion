import pygame

class Ship():
	
	def __init__(self,screen):
		#CLASS CONSTRUCTOR
		self.screen = screen
		
		#load the spaceship and get your rect
		self.image = pygame.image.load('image/ship.png')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		
		#start the new spaceship in the center bottom
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
	
	def blitme(self):
		""" DRAW A SPACE SHIP ON THE ACTUAL POSITION """
		self.screen.blit(self.image,self.rect)
