import pygame
import random


class Enemy:
    def __init__(self, color):
        self.color = color
        self.x = random.randint(100, 400)
        self.y = random.randint(100, 400)

        self.height = random.randint(10, 50)
        self.width = random.randint(10, 50)

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def detect_collision(self, player):
        return self.rect.colliderect(player.rect)
