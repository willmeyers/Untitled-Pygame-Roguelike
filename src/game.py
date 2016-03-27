import pygame
from .tools.graphics import Console
from .scenes.titlescene import TitleScene
from .scenes.gamescene import GameScene


class Game:
	def __init__(self):
		pygame.init()

		self.running = True
		self.clock = pygame.time.Clock()

		self.console = Console()
		self.window = pygame.display.get_surface()

		self.title_scene = TitleScene(self)
		self.game_scene = GameScene(self)
		self.current_scene = self.title_scene

	def update(self):
		self.console.update()
		self.current_scene.update()

	def render(self):
		self.current_scene.render(self.window)
		pygame.display.flip()

	def handle_events(self):
		self.current_scene.handle_events(pygame.event.get())

	def run(self):
		self.update()
		self.render()
		self.handle_events()
		self.clock.tick(60)

	def quit(self):
		self.running = False
		pygame.quit()
