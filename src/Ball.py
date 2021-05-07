import pygame

from pygame import Rect
from pygame.math import Vector2


class Ball:
    def __init__(self, screen_W, screen_H):
        """
        Ball instanciation
        """
        HEIGHT = screen_H // 100  # Player height
        WIDTH = HEIGHT  # Ball width

        self.screen_W = screen_W
        self.screen_H = screen_H

        self.rect = Rect(
            screen_W // 2 - WIDTH // 2,  # Horizontal position
            screen_H // 2 - HEIGHT // 2,  # Vertical position
            WIDTH,  # Width
            HEIGHT,  # Height
        )

        self.radius = HEIGHT // 2
        self.direction = Vector2(0, 1)
        self.speed = 0.2

    def move(self, player, dt):
        """
        Collision check to update direction, and update self.rect accordingly
        """
        # Player collision check
        if self.rect.colliderect(player.rect):
            ball_center = self.rect.left + self.radius
            player_center = player.rect.left + player.rect.width // 2
            coeff = (ball_center - player_center) / player.rect.width
            self.direction = -self.direction
            self.direction.x = coeff * 1.5

        # Top wall collision check
        if self.rect.top < 1:
            self.direction = 2 * Vector2(0, 1) + self.direction

        # Left wall collision check
        if self.rect.left < 1:
            self.direction = 2 * Vector2(1, 0) + self.direction

        # Right wall collision check
        if self.rect.left + self.rect.width > self.screen_W - 1:
            self.direction = 2 * Vector2(-1, 0) + self.direction

        self.direction = self.direction.normalize()

        # Update position
        self.rect.left += self.direction.x * self.speed * dt
        self.rect.top += self.direction.y * self.speed * dt

        return False

    def draw(self, window):
        """
        Draw ball
        """
        center = (self.rect.left + self.radius, self.rect.top + self.radius)
        pygame.draw.circle(window, (255, 0, 0), center, self.radius)
