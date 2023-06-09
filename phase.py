from player import Player
from enemy import Enemy

import pygame


class Phase:
    def __init__(self, player, background, pos, end_pos, d_x, d_y, enemies_amount):
        self.player = player
        self.background = pygame.image.load(background).convert()
        self.pos = pos
        self.end_pos = end_pos
        self.tolerance = 0.5
        self.d_x = d_x
        self.d_y = d_y
        self.color = (0, 0, 100)
        self.enemies = [Enemy((205, 92, 92), [pos, end_pos], True)
                        for i in range(enemies_amount)]

    def tolerance_ok(self):
        if ((self.player.rect.x - self.end_pos[0])**2 <= self.tolerance) and ((self.player.rect.y - self.end_pos[1])**2 <= self.tolerance):
            return True
        else:
            return False

    def detect_collision(self):
        return any([self.player.rect.colliderect(enemy.rect) for enemy in self.enemies])
