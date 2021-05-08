import pygame

from pygame import Rect
from pygame.math import Vector2


class Ball:
    def __init__(self, screen_W, screen_H):
        """
        Ball instanciation
        """
        self.HEIGHT = screen_H // 100  # Player height
        self.WIDTH = self.HEIGHT  # Ball width

        self.screen_W = screen_W
        self.screen_H = screen_H

        self.rect = Rect(
            screen_W // 2 - self.WIDTH // 2,  # left
            screen_H // 2 - self.HEIGHT // 2,  # top
            self.WIDTH,  # width
            self.HEIGHT,  # height
        )

        self.radius = self.HEIGHT // 2
        self.direction = Vector2(0, 1)
        self.speed = 0.2

    def reset_pos(self):
        """
        Reset ball position to beginning
        """
        self.rect.top = self.screen_H // 2 - self.HEIGHT // 2
        self.rect.left = self.screen_W // 2 - self.WIDTH // 2
        self.direction = Vector2(0, 1)

    def move(self, player, blocks, dt):
        """
        Collision check to update direction, and update self.rect accordingly
        """
        # Bottom wall collision detection : game over
        if self.rect.top + self.rect.height > self.screen_H:
            return True

        # Player collision check
        if self.rect.colliderect(player.rect):
            ball_center = self.rect.left + self.radius
            player_center = player.rect.left + player.rect.width // 2
            coeff = (ball_center - player_center) / player.rect.width
            self.direction = -self.direction
            self.direction.x = coeff * 1.5

        # Block collision
        for block in blocks:
            if self.rect.colliderect(block):
                new_direction = self.direction

                # Vertical
                if (
                    block.rect.left
                    < self.rect.left + self.radius
                    < block.rect.left + block.rect.width
                ):
                    # Bottom collision
                    if block.rect.top + block.rect.height * 4 / 5 < self.rect.top:
                        new_direction = Vector2(0, 1)

                    # Top collision
                    else:
                        print("TOP COLLISION")
                        new_direction = Vector2(0, -1)

                # Horizontal
                if (
                    block.rect.top
                    < self.rect.top + self.radius
                    < block.rect.top + block.rect.height
                ):
                    # Right collision
                    if block.rect.left + block.rect.width * 4 / 5 < self.rect.left:
                        new_direction = Vector2(1, 0)

                    # Left collision
                    else:
                        new_direction = Vector2(-1, 0)

                self.direction = 2 * new_direction + self.direction
                block.remove()

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
