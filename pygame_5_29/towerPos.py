import pygame
from settings import *
from mainTower import *
from tower_type import *
towerColor = (132,66,98)
class TowerPosition:
    def __init__(self,surf,x,y,width,height):
        self.image1 = pygame.transform.scale(pygame.image.load("images/pit3.png"),(width,height))
        self.image2 = pygame.transform.scale(pygame.image.load("images/pit1.png"), (65,65))
        self.image = self.image1
        self.x = x
        self.y = y
        self.rect = self.image.get_rect(center=(x,y))
        self.levelrect = self.image.get_rect(center=(x, y))
        self.font = pygame.font.Font("New-Super-Mario-Font-U-1.ttf", 20)

        self.focus = False
        #surf.blit(self.image, (self.rect.x, self.rect.y))
        self.haveTower = False
        self.towerType = None
        self.towerlevel = 1
        self.clicked = False
    def update(self):
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.levelrect = self.image.get_rect(center=(self.x + 50, self.y + 50))

        pass
    def check_hp(self):
        if self.towerType.hp <=0:
            self.towerType = None
            self.image = self.image1
    def draw_level(self, surf):
        my_text = self.font.render(str(self.towerlevel), True, WHITE)
        surf.blit(my_text, self.levelrect)
    def draw(self,surf):
        self.update()
        pos = pygame.mouse.get_pos()  ##得到滑鼠的位置
        if 0<=pos[0]<=1024 and 0<=pos[1]<=425 and self.towerType ==None: ##非選單內且無塔

            if self.rect.collidepoint(pos) and pygame.mouse.get_pressed()[0] == 1:
                self.image = self.image2
                self.focus = True

            elif (not self.rect.collidepoint(pos)) and pygame.mouse.get_pressed()[0] == 1:
                #print("!!!")
                self.image = self.image1
                self.focus = False

        if self.towerType: ##有塔就畫塔
            self.towerType.draw(surf)
            self.check_hp()
            self.draw_level(surf)
        else: ##沒塔就畫自己
            surf.blit(self.image, self.rect)
        return self.focus





