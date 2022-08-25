import pygame
from settings import *
class Anima:
    def __init__(self,x,y,anim):
        self.x = x
        self.y = y
        self.animation_index = 0
        self.anim = anim
        self.image = self.anim[0]
        self.rect = self.image.get_rect(center=(x,y))

    def animate(self, surf):
        self.animation_index += 0.2

        if self.animation_index >= len(self.anim):

            self.animation_index = 0
        self.image = self.anim[int(self.animation_index)]
        self.rect = self.image.get_rect(center=(self.x, self.y))
        surf.blit(self.image, self.rect)
        pass
