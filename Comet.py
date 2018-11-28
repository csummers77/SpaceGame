import pygame
from pygame.sprite import Sprite
from random import randint

class Comet(Sprite):
    def __init__(self):
        super(Comet,self).__init__()
        self.x = 0
        self.y = randint(1,480)
        self.speed = randint(-3,-1)
        self.rect = pygame.Rect(0,0,64,64)
        self.rect.centerx = self.x
        self.rect.top = self.y
        self.damage = 2
    def update_me(self, var = randint(1,2)):
        if var ==1:
            self.y+=self.speed
        else:
            self.y-=self.speed