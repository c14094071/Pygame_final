import pygame
from settings import *
from mainTower import *
from tower_type import *
towerColor = (132,66,98)
class TowerPosition:
    def __init__(self,surf,x,y,width,height):
        self.image1 = pygame.transform.scale(pygame.image.load("images/pit1.png").convert_alpha(),(width,height))
        self.image2 = pygame.transform.scale(pygame.image.load("images/pit2.png").convert_alpha(), (width, height))
        self.image = self.image1
        self.x = x
        self.y = y
        self.rect = self.image.get_rect(center=(x,y))

        self.focus = False
        #surf.blit(self.image, (self.rect.x, self.rect.y))
        self.haveTower = False
        self.towerType = None
    def update(self):
        self.rect = self.image.get_rect(center=(self.x, self.y))

        pass
    def check_hp(self):
        if self.towerType.hp <=0:
            self.towerType = None
            self.image = self.image1
    def draw(self,surf):
        self.update()
        pos = pygame.mouse.get_pos()  ##得到滑鼠的位置
        if 0<=pos[0]<=1024 and 0<=pos[1]<=400 and self.towerType ==None: ##非選單內且無塔
            if self.rect.collidepoint(pos) and pygame.mouse.get_pressed()[0] == 1:
                self.image = self.image2
                self.focus = True

            elif not(self.rect.collidepoint(pos)) and pygame.mouse.get_pressed()[0] == 1:
                self.image = self.image1
                self.focus = False
        if self.towerType:
            self.towerType.draw(surf)
            self.check_hp()
        surf.blit(self.image, self.rect)
        return self.focus



