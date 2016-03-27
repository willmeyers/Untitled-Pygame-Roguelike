import pygame


class InputStream:
	def __init__(self):
		self.valid_inputs = "abcdefgihjklmnopqrstuvwxyz0123456789"
		self.stream = []

	def get_key(self, events):
		for e in events:
			if e.type == pygame.KEYDOWN:
				if chr(e.key) in self.valid_inputs:
					self.stream.append(chr(e.key))

				if e.key == pygame.K_SPACE:
					self.stream.append(' ')

				if e.key == pygame.K_BACKSPACE:
					if self.stream:
						self.stream.pop()

	def reset_stream(self):
		self.stream = []

	def get_stream(self):
		return self.stream
