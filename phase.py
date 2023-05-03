from player import Player


import pygame


class Phase:
    def __init__(self, player, background, pos, end_pos, d_x, d_y):
        self.player = player
        self.background = pygame.image.load(background).convert()
        self.pos = pos
        self.end_pos = end_pos
        self.tolerance = 0.5
        self.d_x = d_x
        self.d_y = d_y

    def tolerance_ok(self):
        if ((self.player.x - self.end_pos[0])**2 <= self.tolerance) and ((self.player.y - self.end_pos[1])**2 <= self.tolerance):
            return True
        else:
            return False

