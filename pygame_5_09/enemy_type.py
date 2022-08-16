import pygame
import os
from enemy import Enemy
import time
frog_anim = []
for i in range(3):
    frog_anim.append(pygame.transform.scale(pygame.image.load(os.path.join('images/frog.jpg')), (60, 60)))
bird_anim = []
for i in range(3):
    bird_anim.append(pygame.transform.scale(pygame.image.load(os.path.join('images/bird.jfif')), (60, 60)))
badguy_anim =[]
for i in range(3):
    badguy_anim.append(pygame.transform.scale(pygame.image.load(os.path.join('images/badguy.png')), (60, 60)))

#第一種怪
class Water(Enemy):
    def __init__(self):
        super().__init__()
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
    def __init__(self):
        super().__init__()  # 繼承Enemy的屬性
        self.hp = 10  # 繼承Enemy的屬性
        self.max_hp = 20
        self.atk = 3
        self.att_range = 200
        self.cd_time = 2  # Unit : seconds
        self.last_cd = time.time() - 2
        self.money = 50
        self.animation = bird_anim[:]

class Badguy(Enemy):
    def __init__(self):
        super().__init__() # 繼承Enemy的屬性
        self.hp = 10  # 繼承Enemy的屬性
        self.max_hp = 8
        self.atk = 4
        self.att_range = 400
        self.cd_time = 0.5  # Unit : seconds
        self.last_cd = time.time() - 0.5
        self.money = 100
        self.animation = badguy_anim[:]


    pass

