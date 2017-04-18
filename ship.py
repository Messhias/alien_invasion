import pygame

class Ship():
	
	def __init__(self,ai_settings,screen):
		#CLASS CONSTRUCTOR
		self.screen = screen
		self.ai_settings = ai_settings
		
		#load the spaceship and get your rect
		self.image = pygame.image.load('image/ship.png')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		
		#store a decimal value for spaceship center 
		self.center = float(self.rect.centerx)
		
		#moviment flag
		self.moving_right = False
		self.moving_left = False
		
		#start the new spaceship in the center bottom
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
	
	def blitme(self):
		""" DRAW A SPACE SHIP ON THE ACTUAL POSITION """
		self.screen.blit(self.image,self.rect)
	
	def update(self):
		''' UPDATE THE POSITION OF SPACE SHIP ACCORDING WITH MOVIMENT FLAG '''
		if self.moving_right:
			self.rect.centerx += 1
		if self.moving_left:
			selft.rect.centerx -=1
			
		#update the object rect according with self.center
		self.rect.centerx = self.center
			
