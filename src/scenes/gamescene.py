import pygame
from src.player import Player
from src.world.world import World
from src.tools.graphics import WorldViewport


class GameScene:
	def __init__(self, game):
		self.game = game
		self.world = World()

		self.world_viewport = WorldViewport(self.world.world_map)

		self.player_command = ""

	def update(self):
		self.world.update()

	def render(self, window):
		window.fill((0, 0, 0))
		self.world_viewport.render(window)
		self.game.console.render_string(window, self.game.console.instream, 10, 460, cursor=True)
		self.world.render(window)

	def handle_events(self, events):
		self.game.console.input.get_key(events)
		for e in events:
			if e.type == pygame.QUIT:
				self.game.running = False

			if e.type == pygame.KEYDOWN and e.key == pygame.K_RETURN:
				self.player_command = self.game.console.input.get_stream()
				self.player_command = ''.join(self.player_command)
				self.execute_command(self.player_command)

				self.game.console.input.reset_stream()

	def execute_command(self, command):
		callbacks = {
			"quit": self.game.quit,
			"clear": self.game.console.clear,
			"north": self.world.player.move_north,
			"south": self.world.player.move_south,
			"east": self.world.player.move_east,
			"west": self.world.player.move_west,
		}

		callbacks[command]()
