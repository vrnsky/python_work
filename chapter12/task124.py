import pygame
import sys
bg_color = (230, 230, 230)

def run_game():
	pygame.init()
	screen = pygame.display.set_mode((1200, 800))
	screen.fill(bg_color);
	pygame.display.set_caption("Task 12 - 4")

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type == pygame.KEYDOWN:
				print(event.key)

run_game()