import sys
import pygame

def check_events(rocket):
	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			check_events_keydown(rocket, event)
			check_events_keyup(rocket, event)
			
			

def check_events_keyup(rocket, event):
	if event.type == pygame.KEYUP:
		if event.key == pygame.K_RIGHT:
			rocket.moving_right = False
		elif event.key == pygame.K_LEFT:
			rocket.moving_left = False
		elif event.key == pygame.K_UP:
			rocket.moving_up = False
		elif event.key == pygame.K_DOWN:
			rocket.moving_down = False


def check_events_keydown(rocket, event):
	if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_RIGHT:
			rocket.moving_right = True
		elif event.key == pygame.K_LEFT:
			rocket.moving_left = True
		elif event.key == pygame.K_UP:
			rocket.moving_up = True
		elif event.key == pygame.K_DOWN:
			rocket.moving_down = True