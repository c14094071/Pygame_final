import pygame
import os
from enemy import Enemy
import time
frog_anim = []
for i in range(3):
    frog_anim.append(pygame.transform.scale(pygame.image.load(os.path.join('images/frog.jpg')), (60, 60)))
bird_anim = []
badguy_anim =[]

#第一種怪
class Water(Enemy):
    def __init__(self, max_hp):
        super().__init__(max_hp)
        self.hp = 10        # 繼承Enemy的屬性
        self.max_hp = 10
        self.money = 20
        self.atk = 2
        self.att_range = 100
        self.cd_time = 1  # Unit : seconds
        self.last_cd = time.time() - 1
        self.animation = frog_anim[:]
#第二種怪
class Egret(Enemy):
    def __init__(self , max_hp):
        super().__init__(max_hp)  # 繼承Enemy的屬性
        self.hp = 10  # 繼承Enemy的屬性
        self.max_hp = 10
        self.atk = 2
        self.att_range = 100
        self.cd_time = 1  # Unit : seconds
        self.last_cd = time.time() - 1
        self.money = 50
        self.animation = bird_anim[:]

class Badguy(Enemy):
    def __init__(self , max_hp):
        super().__init__(max_hp) # 繼承Enemy的屬性
        self.hp = 10  # 繼承Enemy的屬性
        self.max_hp = 10
        self.atk = 2
        self.att_range = 100
        self.cd_time = 1  # Unit : seconds
        self.last_cd = time.time() - 1
        self.money = 100
        self.animation = badguy_anim[:]


    pass

