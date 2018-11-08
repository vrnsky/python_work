import pygame
from rocket_settings import RocketSettings
from rocket import Rocket
import game_functions as gf

bg_color = (230, 230, 230)

def run_game():
	pygame.init()
	settings = RocketSettings()
	screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
	screen.fill(settings.bg_color);
	rocket = Rocket(screen, settings)
	pygame.display.set_caption("Alien Invasion")

	while True:
		gf.check_events(rocket)
		rocket.update()
		rocket.blitme()
		pygame.display.flip()

run_game()