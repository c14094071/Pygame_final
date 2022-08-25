import pygame
from towerPos import *
import os

upgrade_button = pygame.transform.scale(pygame.image.load(os.path.join("images/levelup_button.png")), (50, 50))

class Button:
    def __init__(self, x, y, image):

        width = image.get_width()
        height = image.get_width()
        self.image = image
        #self.image = pygame.transform.scale(image, (int(width * scalex), int(height * scaley)))
        self.rect = self.image.get_rect(center=(x, y))

        self.clicked = False  ##用來判斷有沒有點擊過
    def clickbtn(self):
        pass

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        self.action = False
        pos = pygame.mouse.get_pos()  ##得到滑鼠的位置


        if self.rect.collidepoint(pos):  ##當滑鼠的位置進入到此按鈕的範圍
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:  ##滑鼠按下左鍵[0]
                print("TrueINS")
                self.clicked = True
                self.action = True
        if pygame.mouse.get_pressed()[0] == 0:

            self.clicked = False

          ##作畫

        return self.action


class TowerButton:  ##塔的按鈕
    def __init__(self, x, y, image, scale, CLS):
        self.width = image.get_width()
        self.height = image.get_width()
        self.image = pygame.transform.scale(image, (int(self.width * scale), int(self.height * scale)))
        self.clicked = False  ##用來判斷有沒有點擊過
        self.rect = self.image.get_rect(center=(x, y))
        #self.CLS = CLS
        self.buttonlevel = 1
        self.levelrect = self.image.get_rect(center=(x + 50, y + 50))
        self.font = pygame.font.Font("New-Super-Mario-Font-U-1.ttf", 20)


    def draw_level(self, surf):
        my_text = self.font.render(str(self.buttonlevel), True, WHITE)
        surf.blit(my_text, self.levelrect)

    def put_towerType_ct(self, tp):
        tp.towerType = Cart(tp.x, tp.y, self.buttonlevel)
        return tp.towerType.cost

    def put_towerType_sh(self, tp):
        tp.towerType = Shovel(tp.x, tp.y, self.buttonlevel)
        return tp.towerType.cost

    def put_towerType_gg(self, tp):
        tp.towerType = Goodguy(tp.x, tp.y, self.buttonlevel)
        return tp.towerType.cost

    def put_towerType_pp(self, tp):
        tp.towerType = Pump(tp.x, tp.y, self.buttonlevel)
        return tp.towerType.cost





class CartButton(TowerButton):
    def __init__(self, x, y, image, scale, CLS):
        # super().__init__()
        self.image = cart_anim[0]
        self.width = image.get_width()
        self.height = image.get_width()
        self.levelrect = self.image.get_rect(center=(x + 40, y + 40))
        self.font = pygame.font.Font("New-Super-Mario-Font-U-1.ttf", 20)
        self.buttonlevel = 1

        self.clicked = False  ##用來判斷有沒有點擊過
        self.rect = self.image.get_rect(center=(x, y))
        self.CLS = CLS
    def draw(self,money, surface):
        # print(pos[0],pos[1])
        surface.blit(self.image, self.rect)
        self.draw_level(surface)




class PumpButton(TowerButton):
    def __init__(self, x, y, image, scale, CLS):
        # super().__init__()

        self.image = pump_anim[0]
        self.width = image.get_width()
        self.height = image.get_width()
        self.levelrect = self.image.get_rect(center=(x + 50, y + 50))
        self.font = pygame.font.Font("New-Super-Mario-Font-U-1.ttf", 20)
        self.buttonlevel = 1
        self.clicked = False  ##用來判斷有沒有點擊過
        self.rect = self.image.get_rect(center=(x, y))
        self.CLS = CLS

    def draw(self, money, surface):

        surface.blit(self.image, self.rect)
        self.draw_level(surface)



class GoodguyButton(TowerButton):
    def __init__(self, x, y, image, scale, CLS):
        # super().__init__()

        self.image = goodguy_anim[0]
        self.width = image.get_width()
        self.height = image.get_width()
        self.levelrect = self.image.get_rect(center=(x + 50, y + 50))
        self.font = pygame.font.Font("New-Super-Mario-Font-U-1.ttf", 20)
        self.buttonlevel = 1
        self.clicked = False  ##用來判斷有沒有點擊過
        self.rect = self.image.get_rect(center=(x, y))
        self.CLS = CLS

    def draw(self, money, surface):

        # print(pos[0],pos[1])
        surface.blit(self.image, self.rect)
        self.draw_level(surface)
class ShovelButton(TowerButton):
    def __init__(self, x, y, image, scale, CLS):
        # super().__init__()

        self.image = shovel_anim[0]
        self.width = image.get_width()
        self.height = image.get_width()
        self.levelrect = self.image.get_rect(center=(x + 50, y + 50))
        self.font = pygame.font.Font("New-Super-Mario-Font-U-1.ttf", 20)
        self.buttonlevel = 1
        self.clicked = False  ##用來判斷有沒有點擊過
        self.rect = self.image.get_rect(center=(x, y))
        self.CLS = CLS

    def draw(self, money, surface):

        # print(pos[0],pos[1])
        surface.blit(self.image, self.rect)
        self.draw_level(surface)



class Upgradebutton:
    def __init__(self, x: int, y: int):
        self.image = upgrade_button
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def clicked(self, x, y):
        #print("YYYYYY")
        return True if self.rect.collidepoint(x, y) else False

    def draw(self, win):
        win.blit(self.image, self.rect)
class BreakTowerButton:
    def __init__(self, x: int,y:int):
        self.image = pygame.transform.scale(pygame.image.load(os.path.join("images/skill_2.png")), (80, 80))
        self.rect = self.image.get_rect(center=(x,y))
    def clicked(self):
        pos = pygame.mouse.get_pos()
        return True if self.rect.collidepoint(pos[0],pos[1]) and pygame.mouse.get_pressed()[
                0] == 1 else False
    def draw(self,surf):
        surf.blit(self.image,self.rect)
    def breaktower(self):

        if self.clicked():
            for tp in towerposiList:
                if tp.towerType:
                    if tp.towerType.drawcircle == True:
                        tp.towerType = None
                        tp.image = tp.image1
                        tp.focus = False

class CleanWaterButton:
    def __init__(self,x:int, y:int):
        self.image = pygame.transform.scale(pygame.image.load(os.path.join("images/skill_1.png")), (80, 80))
        self.rect = self.image.get_rect(center=(x, y))
        self.clicked1 = False
        self.action = True

    def clicked(self):
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[
                0] == 1 and self.clicked1 == False:  ##滑鼠按下左鍵([0]==1) 且塔還沒按過(self.clicked = False)

                self.clicked1 = True
                return True
            if pygame.mouse.get_pressed()[0] == 0:  ##當手放開左鍵
                self.clicked1 = False  ##狀態變回塔還沒按過

    def draw(self,surf):
        surf.blit(self.image,self.rect)


