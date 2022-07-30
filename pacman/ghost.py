import pygame.draw
from game import Game


class Ghost(Game):
    def __init__(self, cor, size):
        self.column = 6
        self.line = 8
        self.cor = cor
        self.size = size

    def process_events(self, events):
        pass

    def process_rules(self):
        pass

    def draw(self, screen):
        slice = self.size // 8
        px = int(self.column * self.size)
        py = int(self.line * self.size)
        contorno = [
            (px, py + self.size),
            (px + slice, py + slice * 2),
            (px + slice * 3, py + slice // 3),
            (px + slice * 3, py),
            (px + slice * 5, py),
            (px + slice * 6, py + slice // 2),
            (px + slice * 7, py + slice * 2),
            (px + self.size, py + self.size)
        ]
        pygame.draw.polygon(screen, self.cor, contorno, 0)