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
		
		#start the new spaceship in the center bottom
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		
		#stores decimal value for spaceship in the inner
		self.center = float(self.rect.centerx)
		
		
		#moviment flag
		self.moving_right = False
		self.moving_left = False
		
	
	def blitme(self):
		""" DRAW A SPACE SHIP ON THE ACTUAL POSITION """
		self.screen.blit(self.image,self.rect)
	
	def update(self):
		''' 
			UPDATE THE POSITION OF SPACE SHIP ACCORDING WITH MOVIMENT FLAG
			AND PREVENTS THE SAME GO OUT THE BORDERS
		 '''
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.ai_settings.ship_speed_factor
		if self.moving_left and self.rect.left > 0:
			self.center -= self.ai_settings.ship_speed_factor
			
		#update the object rect according with self.center
		self.rect.centerx = self.center
			
