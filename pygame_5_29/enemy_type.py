import pygame
import os
from enemy import Enemy
from settings import *
import time


#第一種怪:水
class Water(Enemy):
    def __init__(self, level):
        super().__init__(level=level,hp_list=water_hp_list,max_hp_list=water_max_hp_list,
                         atk_list=water_atk_list,range_list=water_range_list,cd_time_list=water_cd_time_list,
                         money=10, animation=water_anim)


#第三種怪:壞釣客
class Badguy(Enemy):
    def __init__(self, level):
        super().__init__(level=level,hp_list=badguy_hp_list,max_hp_list=badguy_max_hp_list,
                         atk_list=badguy_atk_list,range_list=badguy_range_list,cd_time_list=badguy_cd_time_list,
                         money=50,animation=badguy_anim[:]) # 繼承Enemy的屬性
class DirtyWater(Enemy):
    def __init__(self,level):
        super().__init__(level=level,hp_list=dirtywater_hp_list,max_hp_list=dirtywater_max_hp_list,
                         atk_list=dirtywater_atk_list,range_list=dirtywater_range_list,
                         cd_time_list=dirtywater_cd_time_list,money=20,animation=dirtywater_anim)
class DeadFish(Enemy):
    def __init__(self,level):
        super().__init__(level=level,hp_list=deadfish_hp_list,max_hp_list=deadfish_max_hp_list,
                         atk_list=deadfish_atk_list,range_list=deadfish_range_list,
                         cd_time_list=deadfish_cd_time_list,money=25,animation=deadfish_anim)
class Stone(Enemy):
    def __init__(self,level):
        super().__init__(level=level,hp_list=stone_hp_list,max_hp_list=stone_max_hp_list,
                         atk_list=stone_atk_list,range_list=stone_range_list,
                         cd_time_list=stone_cd_time_list,money=20,animation=stone_anim)

class Boss01(Enemy):
    def __init__(self):
        self.width = 200
        self.height = 200
        self.hp = 100
        self.max_hp = 100
        self.atk = 8
        self.att_range = 400
        self.cd_time = 0.9
        self.money = 200
        self.last_cd = time.time() - 0.9
        # update (move)
        self.path = PATH
        self.path_index = 0
        self.move_count = 0
        self.stride = 1
        self.x = self.path[0][0]
        self.y = self.path[0][1]
        self.image = None
        self.animation = boss01_anim
        self.animation_index = 0
        self.last_update = time.time()
        self.frame_rate = 1
        ##

class Boss02(Enemy):
    def __init__(self):
        self.width = 200
        self.height = 200
        self.hp = 700
        self.max_hp = 700
        self.atk = 10
        self.att_range = 500
        self.cd_time = 1
        self.money = 1000
        self.last_cd = time.time() - 1
        # update (move)
        self.path = PATH
        self.path_index = 0
        self.move_count = 0
        self.stride = 1
        self.x = self.path[0][0]
        self.y = self.path[0][1]
        self.image = None
        self.animation = boss02_anim
        self.animation_index = 0
        self.last_update = time.time()
        self.frame_rate = 1
        ##





