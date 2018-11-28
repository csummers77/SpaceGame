import pygame
import os
from pygame.sprite import Sprite

pygame.display.set_mode((620, 480))

class Laser(Sprite):
    def __init__(self,x,y):
        super(Laser,self).__init__()
        self.image = pygame.transform.scale(laser_image, (20,50))
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedx = 10
    def update_me(self):
        self.rect.x += self.speedx
        if self.rect.bottom < 0:
            self.kill()