import pygame

from pygame import Rect


class Player:
    def __init__(self, screen_W, screen_H):
        """
        Player instanciation
        """
        WIDTH = screen_W // 10  # Player width
        HEIGHT = screen_H // 100  # Player height

        self.screen_W = screen_W
        self.screen_H = screen_H

        self.init_pos_left = screen_W // 2 - WIDTH // 2
        self.init_pos_top = screen_H * 5 / 6

        self.rect = Rect(
            self.init_pos_left,  # left
            self.init_pos_top,  # top
            WIDTH,  # width
            HEIGHT,  # height
        )

        self.speed = 1

    def reset_pos(self):
        """
        Reset player position to beginning
        """
        self.rect[0] = self.init_pos_left  # left
        self.rect[1] = self.init_pos_top  # top

    def move(self, keys, dt):
        """
        Keyboard controls
        """
        if keys[pygame.K_a] and self.rect.left > 0:
            self.rect.left -= self.speed * dt
        if (
            keys[pygame.K_d]
            and self.rect.left + self.rect.width < self.screen_W
        ):
            self.rect.left += self.speed * dt

    def draw(self, window):
        """
        Draw rectangle
        """
        pygame.draw.rect(window, (255, 255, 255), self.rect)
