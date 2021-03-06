import pygame
import level
import wall

class CharObject():
    def __init__(self, x, y, player_num):
        self.x = x
        self.y = y
        self.x_spd = 0
        self.y_vel = 0
        self.max_spd = 20
        self.max_vel = 36
        self.len = 32
        self.jumps = 2
        if player_num == 1:
            self.color = [0, 0, 255]
        elif player_num == 2:
            self.color = [255, 0, 0]
        self.rectangle = pygame.Rect([self.x, self.y, self.len, self.len])

    def draw(self, s):
        pygame.draw.rect(s, self.color, self.rectangle)

    def jump(self, vel):
        if self.jumps > 0:
            self.y_vel = vel
            self.jumps -= 1

    def move(self, spd):
        if self.x_spd < self.max_spd and self.x_spd > -self.max_spd:
            self.x_spd += spd

    def update(self):
        if self.x_spd > 0:
            self.x_spd -= 2
        elif self.x_spd < 0:
            self.x_spd += 2
        if self.y_vel < self.max_vel:
            self.y_vel += 6
        self.rectangle = pygame.Rect([self.x, self.y, self.len, self.len])
        print(self.jumps)

    def final_loc(self):
        self.y += self.y_vel
        self.x += self.x_spd
        self.rectangle = pygame.Rect([self.x, self.y, self.len, self.len])

    def collide(self, target):
        while pygame.Rect([self.x, self.y + self.y_vel, self.len, self.len]).colliderect(target):
            if self.y_vel > 0:
                self.jumps = 2
                self.y_vel -= 1
            if self.y_vel < 0:
                self.y_vel += 1
            #self.rectangle = pygame.Rect([self.x, self.y, 16, 16])

        while pygame.Rect([self.x + self.x_spd, self.y + self.y_vel, self.len, self.len]).colliderect(target):
            if self.x_spd > 0:
                self.x_spd -= 1
            if self.x_spd < 0:
                self.x_spd += 1
