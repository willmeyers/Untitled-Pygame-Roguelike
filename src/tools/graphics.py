import pygame
from .stream import InputStream


class WorldViewport:
	def __init__(self, world_view):
		self.world_view = world_view
		self.tile_sheet = pygame.image.load("resources/default_tileset.png")

		self.tiles = {
			0: self.get_tile_surface(192, 32),
			1: self.get_tile_surface(192, 0),
			2: self.get_tile_surface(224, 32),
			3: self.get_tile_surface(192, 64),
			4: self.get_tile_surface(160, 32),
			5: self.get_tile_surface(160, 0),
			6: self.get_tile_surface(224, 0),
			7: self.get_tile_surface(224, 64),
			8: self.get_tile_surface(160, 64),
			9: self.get_tile_surface(0, 0)
		}

	def render(self, window):
		x = 0
		y = 0
		for row in self.world_view:
			for col in row:
				window.blit(self.tiles[col], (x, y))
				x += 32
			x = 0
			y += 32

	def get_tile_surface(self, posx, posy):
		tile = pygame.Surface([32, 32])
		tile.blit(self.tile_sheet, (0, 0), (posx, posy, 32, 32))

		return tile

class Console:
	def __init__(self):
		self.input = InputStream()
		self.instream = self.input.get_stream()
		self.cursor = pygame.Surface([10, 10])
		self.cursor.fill((0, 255, 0))

		pygame.display.set_mode((680, 480))
		pygame.display.set_caption("The Text Adventure")

		self.font_sheet = pygame.image.load("resources/font.png").convert()
		self.characters = {
			'a': self.get_character_surface(0, 0),
			'b': self.get_character_surface(10, 0),
			'c': self.get_character_surface(20, 0),
			'd': self.get_character_surface(30, 0),
			'e': self.get_character_surface(40, 0),
			'f': self.get_character_surface(50, 0),
			'g': self.get_character_surface(60, 0),
			'h': self.get_character_surface(70, 0),
			'i': self.get_character_surface(80, 0),
			'j': self.get_character_surface(90, 0),
			'k': self.get_character_surface(100, 0),
			'l': self.get_character_surface(110, 0),
			'm': self.get_character_surface(120, 0),
			'n': self.get_character_surface(130, 0),
			'o': self.get_character_surface(140, 0),
			'p': self.get_character_surface(150, 0),
			'q': self.get_character_surface(160, 0),
			'r': self.get_character_surface(170, 0),
			's': self.get_character_surface(180, 0),
			't': self.get_character_surface(190, 0),
			'u': self.get_character_surface(200, 0),
			'v': self.get_character_surface(210, 0),
			'w': self.get_character_surface(220, 0),
			'x': self.get_character_surface(230, 0),
			'y': self.get_character_surface(240, 0),
			'z': self.get_character_surface(250, 0),
			'0': self.get_character_surface(0, 10),
			'1': self.get_character_surface(10, 10),
			'2': self.get_character_surface(20, 10),
			'3': self.get_character_surface(30, 10),
			'4': self.get_character_surface(40, 10),
			'5': self.get_character_surface(50, 10),
			'6': self.get_character_surface(60, 10),
			'7': self.get_character_surface(70, 10),
			'8': self.get_character_surface(80, 10),
			'9': self.get_character_surface(90, 10),
			' ': self.get_character_surface(100, 10)
		}

	def update(self):
		self.instream = self.input.get_stream()

	def get_character_surface(self, posx, posy):
		char = pygame.Surface([10, 10])
		char.blit(self.font_sheet, (0, 0), (posx, posy, 10, 10))
		char.set_colorkey((0, 0, 0))

		return char

	def get_character(self, character):
		for key, value in self.characters.items():
			if character == key:
				return value

	def render_string(self, window, string, x, y, cursor=False):
		col = 0
		for char in string:
			window.blit(self.get_character(char), (col+x, y))
			col += 10

		if cursor:
			window.blit(self.cursor, (col+x, y))

	def clear(self):
		pass
