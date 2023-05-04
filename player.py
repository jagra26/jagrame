import pygame


class Player:
    def __init__(self, x, y, color, height, width, vel):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.height = height
        self.width = width
        self.vel = vel

    def update_pos(self, x, y):
        if x > 0:
            self.rect.x += self.vel*x
        elif x < 0:
            self.rect.x -= self.vel*(-x)
        if y > 0:
            self.rect.y += self.vel*y
        elif y < 0:
            self.rect.y -= self.vel*(-y)
        return
