
import pygame

from settings import Settings
from ship import Ship
import game_functions  as gf

def run_game():
	#START THE GAME WITH A OBJECT IN THE SCREEN
	pygame.init()
	
	ai_settings = Settings()
	
	screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion!")
	
	#CREATE SPACESHIP
	ship = Ship(ai_settings,screen)
	
	#Start the game
	while True:
		
		gf.check_events(ship)
		ship.update()
		gf.update_screen(ai_settings,screen,ship)
		
		
		
			
	
run_game()
