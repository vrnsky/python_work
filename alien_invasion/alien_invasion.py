import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from alien import Alien
from pygame.sprite import Group
from game_stats import GameStats

bg_color = (230, 230, 230)
# //problems here
def run_game():
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	screen.fill(ai_settings.bg_color);
	ship = Ship(ai_settings, screen)
	aliens = Group()
	gf.create_fleet(ai_settings, screen, ship, aliens)
	pygame.display.set_caption("Alien Invasion")
	bullets = Group()
	stats = GameStats(ai_settings)
	while True:
		gf.check_events(ai_settings, screen, ship, bullets)
		print(str(stats.ship_left))
		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
			gf.update_aliens(ai_settings, stats, screen, aliens, ship, bullets)		

		gf.update_screen(ai_settings, stats, screen, ship, aliens, bullets)

run_game()