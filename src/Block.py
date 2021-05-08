import pygame

from pygame import Rect


class Block:
    def __init__(self, size, left, top, screen_W, screen_H):
        """
        Block instanciation
        """
        self.rect = Rect(
            left,
            top,
            size,
            size
        )

    def remove(self):
        self.rect = Rect(0, 0, 0, 0)

    def draw(self, window):
        pygame.draw.rect(window, (100, 100, 100), self.rect)
