from src.player import Player


class World:
    def __init__(self):
        self.world_map = [
            [5, 1, 1, 1, 1, 1, 1, 6],
            [4, 0, 0, 0, 0, 0, 0, 2],
            [4, 0, 0, 0, 0, 0, 0, 2],
            [4, 0, 0, 0, 0, 0, 0, 2],
            [4, 0, 0, 0, 0, 0, 0, 2],
            [4, 0, 0, 0, 0, 0, 0, 2],
            [4, 0, 0, 0, 0, 0, 0, 2],
            [4, 0, 0, 0, 0, 0, 0, 2],
            [8, 3, 3, 3, 3, 3, 3, 7]
        ]

        self.player = Player("Name")


    def update(self):
        pass

    def render(self, window):
        self.player.render(window)
