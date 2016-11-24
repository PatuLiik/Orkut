import pygame

class WallObject():
    def __init__(self, x, y, length, height):
        self.x = x
        self.y = y
        self.len = length
        self.hei = height
        self.color = [0, 0, 0]
        self.rectangle = pygame.Rect([self.x, self.y, self.len, self.hei])

    def draw(self, s):
        pygame.draw.rect(s, self.color, self.rectangle)

    def update(self):#see pole praegu kasutuses, sest mitte midagi ei liigu
        self.rectangle = pygame.Rect([self.x, self.y, self.len, self.hei])
