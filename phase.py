from player import Player


import pygame


class Phase:
    def __init__(self, player, background, pos, end_pos):
        self.player = player
        self.background = pygame.image.load(background).convert()
        self.pos = pos
        self.end_pos = end_pos
