from src.game import Game


def main():
	game = Game()

	while game.running:
		game.run()

	game.quit()