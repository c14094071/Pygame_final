import pygame
from settings import *
class TowerView:
    def __init__(self,x,y,att_range=None,anim=None,image=None):
        self.x = x
        self.y = y
        self.animation_index =0
        self.att_range = att_range
        self.image = image
        self.anim = anim
        if self.anim:
            self.image = self.anim[0]
        self.rect = self.image.get_rect(center=(x,y))
        self.width = self.rect.width
        self.height = self.rect.height

        pass
    def animate(self,surf):
        self.animation_index += 0.2
        if self.animation_index >= len(self.anim):
            self.animation_index = 0
        self.image = self.anim[int(self.animation_index)]
        surf.blit(self.image, self.rect)
        pass
    def draw_hp_bar(self,surf,hp,max_hp):
        hp_width = self.width * (hp / max_hp)
        pygame.draw.rect(surf, PUR_1, (self.x - self.width // 2, self.y + 55, self.width, 6), 0)
        pygame.draw.rect(surf, PUR_2, (self.x - self.width // 2, self.y + 55, hp_width, 6), 0)
        pass
    def draw_range(self,surf):
        self.surface = pygame.Surface((self.att_range * 2, self.att_range * 2), pygame.SRCALPHA)  ##先畫在透明的畫布上
        self.circle = pygame.draw.circle(self.surface, (128, 128, 128, 100), (self.att_range, self.att_range),
                                         self.att_range)  ##circle rect

        ##在畫布上畫圓
        surf.blit(self.surface, (self.x - self.att_range, self.y - self.att_range))
        pass
