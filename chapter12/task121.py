import pygame
import sys
from fly import Fly

def run_game():
	pygame.init()
	screen = pygame.display.set_mode((1200, 800))
	screen.fill((255,255,255))
	fly = Fly(screen)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

		fly.blitme()
		pygame.display.flip()

run_game()