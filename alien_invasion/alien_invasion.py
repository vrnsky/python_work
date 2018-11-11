import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from alien import Alien
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import ScoreBoard


def run_game():
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	screen.fill(ai_settings.bg_color);
	ship = Ship(ai_settings, screen)
	aliens = Group()
	play_button = Button(ai_settings, screen, "Play")
	gf.create_fleet(ai_settings, screen, ship, aliens)
	pygame.display.set_caption("Alien Invasion")
	bullets = Group()
	stats = GameStats(ai_settings)
	sb = ScoreBoard(ai_settings, screen, stats)
	while True:
		gf.check_events(ai_settings, screen, ship, bullets, play_button, stats, aliens, sb)
		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_settings, screen, ship, aliens, bullets, stats, sb)
			gf.update_aliens(ai_settings, stats, screen, aliens, ship, bullets, sb)		

		gf.update_screen(ai_settings, stats, screen, ship, aliens, bullets, play_button, sb)

run_game()