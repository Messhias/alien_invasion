import sys

import pygame

from settings import Settings
from ship import Ship

def run_game():
	#START THE GAME WITH A OBJECT IN THE SCREEN
	pygame.init()
	
	ai_settings = Settings()
	
	screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion!")
	
	#CREATE SPACESHIP
	ship = Ship(screen)
	
	#Start the game
	while True:
		
		#SCHEDULE KEYBOARD AND MOUSE
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
				
			#show the recentely screen
		
		# fill the screen
		screen.fill(ai_settings.bg_color)
		ship.blitme()
		
		pygame.display.flip()
		
		
			
	
run_game()
