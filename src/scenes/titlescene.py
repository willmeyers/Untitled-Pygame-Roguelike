import pygame


def get_character_surface(sheet, posx, posy):
		char = pygame.Surface([300, 150])
		char.blit(sheet, (0, 0), (posx, posy, 300, 150))
		char.set_colorkey((0, 0, 0))

		return char

class TitleScene:
	def __init__(self, game):
		self.game = game
		self.player_command = ""

		self.sheet = pygame.image.load("resources/font.png").convert()

	def update(self):
		pass

	def render(self, window):
		window.fill((0, 0, 0))
		self.game.console.render_string(window, self.game.console.instream, 10, 460, cursor=True)

	def handle_events(self, events):
		self.game.console.input.get_key(events)
		for e in events:
			if e.type == pygame.QUIT:
				self.game.running = False

			if e.type == pygame.KEYDOWN and e.key == pygame.K_RETURN:
				self.player_command = self.game.console.input.get_stream()
				self.player_command = ''.join(self.player_command)
				self.parse_command(self.player_command)
				self.game.console.input.reset_stream()

	def parse_command(self, cmd):
		if cmd == "quit":
			self.game.running = False

		if cmd ==  "start":
			self.game.current_scene = self.game.game_scene
