import pygame
import random


class Enemy:
    def __init__(self, color, prohibited_areas, is_moving=False):
        self.color = color

        self.height = random.randint(10, 50)
        self.width = random.randint(10, 50)
        self.is_moving = is_moving

        while True:
            self.x = random.randint(100, 400)
            self.y = random.randint(100, 400)
            self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

            self.initial_rect = pygame.Rect(
                prohibited_areas[0][0], prohibited_areas[0][1], 60, 60)
            self.final_rect = pygame.Rect(
                prohibited_areas[1][0], prohibited_areas[1][1], 60, 60)

            if not any([self.rect.colliderect(prohibited_area) for prohibited_area in [self.initial_rect, self.final_rect]]):
                break

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def detect_collision(self, player):
        return self.rect.colliderect(player.rect)
