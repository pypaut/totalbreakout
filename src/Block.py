import pygame

from pygame import Rect


class Block:
    def __init__(self, screen_W, screen_H):
        """
        Block instanciation
        """
        WIDTH = screen_W // 10
        HEIGHT = WIDTH

        self.rect = Rect(
            screen_W // 2 - WIDTH // 2,
            screen_H // 3 - HEIGHT // 2,
            WIDTH,
            HEIGHT,
        )

    def remove(self):
        self.rect = Rect(0, 0, 0, 0)

    def draw(self, window):
        pygame.draw.rect(window, (100, 100, 100), self.rect)
