import pygame
from towerPos import *


class Button:
    def __init__(self, x, y, image, scalex, scaley):

        width = image.get_width()
        height = image.get_width()

        self.image = pygame.transform.scale(image, (int(width * scalex), int(height * scaley)))
        self.rect = self.image.get_rect(center=(x, y))

        self.clicked = False  ##用來判斷有沒有點擊過

    def draw(self, surface):
        action = False
        pos = pygame.mouse.get_pos()  ##得到滑鼠的位置

        if self.rect.collidepoint(pos):  ##當滑鼠的位置進入到此按鈕的範圍
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:  ##滑鼠按下左鍵[0]
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        surface.blit(self.image, self.rect)  ##作畫

        return action


class TowerButton:  ##塔的按鈕
    def __init__(self, x, y, image, scale, CLS):
        self.width = image.get_width()
        self.height = image.get_width()
        self.image = pygame.transform.scale(image, (int(self.width * scale), int(self.height * scale)))
        self.clicked = False  ##用來判斷有沒有點擊過
        self.rect = self.image.get_rect(center=(x, y))
        self.CLS = CLS

    def put_towerType(self, tp, CLS):
        tp.towerType = CLS(tp.x, tp.y)

    def draw(self, surface):
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[
                0] == 1 and self.clicked == False:  ##滑鼠按下左鍵([0]==1) 且塔還沒按過(self.clicked = False)
                for tp in towerposiList:
                    if tp.focus == True:
                        tp.image = self.image
                        self.put_towerType(tp, self.CLS)
                        tp.focus = False
                        # tp.towerType = Castnet(tp.x,tp.y)

                        # tp.haveTower = True
                self.clicked = True  ##已經按了塔
            if pygame.mouse.get_pressed()[0] == 0:  ##當手放開左鍵
                self.clicked = False  ##狀態變回塔還沒按過
        # print(pos[0],pos[1])
        surface.blit(self.image, self.rect)


class CastnetButton(TowerButton):
    def __init__(self, x, y, image, scale, CLS):
        # super().__init__()
        self.width = image.get_width()
        self.height = image.get_width()
        self.image = pygame.transform.scale(image, (int(self.width * scale), int(self.height * scale)))
        self.clicked = False  ##用來判斷有沒有點擊過
        self.rect = self.image.get_rect(center=(x, y))
        self.CLS = CLS


class PumpButton(TowerButton):
    def __init__(self, x, y, image, scale, CLS):
        # super().__init__()
        self.width = image.get_width()
        self.height = image.get_width()
        self.image = pygame.transform.scale(image, (int(self.width * scale), int(self.height * scale)))
        self.clicked = False  ##用來判斷有沒有點擊過
        self.rect = self.image.get_rect(center=(x, y))
        self.CLS = CLS


class GoodguyButton(TowerButton):
    def __init__(self, x, y, image, scale, CLS):
        # super().__init__()
        self.width = image.get_width()
        self.height = image.get_width()
        self.image = pygame.transform.scale(image, (int(self.width * scale), int(self.height * scale)))
        self.clicked = False  ##用來判斷有沒有點擊過
        self.rect = self.image.get_rect(center=(x, y))
        self.CLS = CLS
