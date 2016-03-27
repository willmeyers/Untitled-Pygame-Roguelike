import pygame

class Player:
	def __init__(self, name):
		self.gold = 0
		self.inventory = []

		self.equipment = {
			"HEAD": None,
			"CHEST": None,
			"LEGS": None,
			"FEET": None,
			"WEAPON": None
		}

		self.world_x = 3
		self.world_y = 3

		self.pp = pygame.Surface([32, 32])
		self.pp.fill((255, 255, 0))

	def update(self):
		pass

	def render(self, window):
		window.blit(self.pp, (self.world_x*32, self.world_y*32))

	def move_north(self):
		self.world_y -= 1

	def move_south(self):
		self.world_y += 1

	def move_east(self):
		self.world_x += 1

	def move_west(self):
		self.world_x -= 1
