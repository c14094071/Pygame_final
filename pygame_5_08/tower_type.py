from mainTower import *
import pygame
class Castnet(Tower):
    def __init__(self,x,y):
        super().__init__()
        self.x = x
        self.y = y
        self.image = pygame.transform.scale(pygame.image.load(tower01_img).convert_alpha(),(50,50))
        self.rect = self.image.get_rect(center=(self.x,self.y))
        self.width = self.rect.width
        self.height = self.rect.height
        self.hp = 50
        self.max_hp = 50
        self.atk = 1


class Pump(Tower) :
#在maintower的Tower完成數值
    def __init__(self , x , y):
        #繼承tower
        super().__init__()
        self.x = x
        self.y = y
        '''
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        '''
        self.image = pygame.transform.scale(pygame.image.load(tower01_img).convert_alpha(), (50, 50))
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.width = self.rect.width
        self.height = self.rect.height
        self.hp = 50
        self.max_hp = 50
        self.atk = 1

        self.damage = 5
        self.att_range = 150
        self.cd_time = 0.5

#建立範圍攻擊塔
class Goodguy(Tower) :
    def __init__(self , x , y ):
        super().__init__()
        self.x = x
        self.y = y
        '''
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        '''
        self.image = pygame.transform.scale(pygame.image.load(tower01_img).convert_alpha(), (50, 50))
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.width = self.rect.width
        self.height = self.rect.height
        self.hp = 50
        self.max_hp = 50
        self.atk = 1
        self.damage = 3
        self.att_range = 120
        self.cd_time = 1
#範圍攻擊
    '''
    def attack(self, enemy):
        if not self.is_cool_down():
            for en in enemy:
                if self.is_in_range(en):
                    self.is_update_anim = True
                    en.hp -= self.damage
'''




