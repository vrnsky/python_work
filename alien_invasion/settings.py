﻿class Settings():

	def __init__(self):
		self.screen_width = 1366
		self.screen_height = 768
		self.bg_color = (230, 230, 230)

		# добавляем параметры пулей
		
		self.bullet_width = 300
		self.bullet_height = 15
		self.bullet_color = 60, 60, 60
		self.bullets_allowed = 3

		self.fleet_drop_speed = 80

		self.ship_limit = 3
		self.speedup_scale = 1.1
		self.score_scale = 1.5

		self.init_dynamic_settings()

	def init_dynamic_settings(self):
		self.ship_speed_factor = 1.5
		self.bullet_speed_factor = 1
		self.alien_speed_factor = 1
		#1 - движение вправо | -1 влево
		self.fleet_direction = 1
		self.alien_points = 50
	

	def increase_speed(self):
		self.ship_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale
		self.alien_points = int(self.alien_points * self.score_scale)