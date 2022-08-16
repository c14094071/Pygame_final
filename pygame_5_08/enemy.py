import pygame
import math
import os
import time
from settings import *



class Enemy:
    def __init__(self):
        self.width = 60
        self.height = 60
        self.max_hp = None
        self.hp = None
        self.atk = None
        self.money = 0
        self.last_cd = time.time()-1
        self.cd_time = 1
        # update (move)
        self.path = PATH
        self.path_index = 0
        self.move_count = 0
        self.stride = 1
        self.x = self.path[0][0]
        self.y = self.path[0][1]

        # image and animation
        self.image = None
        self.animation = []
        self.animation_index = 0
        self.last_update = time.time()
        self.frame_rate = 1
        ##

    def is_cool_down(self): ##回傳bool

        self.now = time.time()  ##取得現在的時間
        if self.now - self.last_cd >= self.cd_time:  ##現在的時間減掉上次使用的時間大於等於cd的話 就代表冷卻時間過了
            return False  ##冷卻已過
        else:
            return True  ##還在冷卻

    def is_in_range(self, tower): ##回傳bool


        if math.sqrt((tower.x - self.x) ** 2 + (tower.y - self.y) ** 2) <= self.att_range:  ##此塔的點與敵人的點之間的距離小於等於半徑
            return True  ##代表敵人在此塔的圓圈範圍內
        else:
            return False  ##範圍外

    def update(self,towers):
        """
        Move enemy
        :return: None
        """

        x1, y1 = self.path[self.path_index]
        x2, y2 = self.path[self.path_index + 1]

        # 敵人在固定路徑(self.path)上移動的更新動作

        # compute the distance and max_count between two points
        distance = math.sqrt((x2-x1) ** 2 + (y2-y1) ** 2)
        max_count = int(distance / self.stride)

        # compute the unit vector
        unit_vector_x = (x2-x1) / distance
        unit_vector_y = (y2-y1) / distance

        # compute the movement
        delta_x = unit_vector_x * self.stride
        delta_y = unit_vector_y * self.stride

        # update the position and counter
        if self.move_count <= max_count:
            self.x += delta_x
            self.y += delta_y
            self.move_count += 1
        else:
            self.move_count = 0
            self.path_index += 1
            self.x, self.y = self.path[self.path_index]

        if not self.is_cool_down():  ##當冷卻已過
            for tow in towerposiList:  ##對每個塔做判斷
                if tow.towerType != None and self.is_in_range(tow) and tow.towerType.hp > 0:  ##如果有塔在裡面
                    tow.towerType.hp -= self.atk  ##塔就損血
                    self.last_cd = self.now  ##把使用攻擊的當下時間變成上次使用時間
                    # ---第2題---
                    # 請完成敵人扣血的機制
                    # 可以利用1.self.damage
                    break  # AOE attack (break會有單一攻擊的效果，可以試著拿掉看看會發生什麼事)


        # update the animation count
        now = time.time()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.animation_index += 1
            if self.animation_index < len(self.animation)-1:
                self.image = self.animation[self.animation_index]
            else:
                self.image = self.animation[self.animation_index]
                self.animation_index = 0

    def draw_hp_bar(self, surf):
        """
        draw health bar above enemy
        :param surf: surface
        :return: None
        """
        # 敵人的血條，血條位置始終位於敵人頭上(要能夠根據敵人位置而去更新血條位置)
        hp_width = self.width * (self.hp / self.max_hp)
        pygame.draw.rect(surf, RED_1, [self.x - self.width // 2, self.y - self.height // 2 - 5, self.width, 6], 0)
        pygame.draw.rect(surf, RED_2, [self.x - self.width // 2, self.y - self.height // 2 - 5, hp_width, 6], 0)



    def draw(self, surf):
        """
        Draws the enemy with the given images
        :param surf: surface
        :return: None
        """
        self.image = self.animation[self.animation_index]
        surf.blit(self.image, (self.x - self.width // 2, self.y - self.height // 2))
        self.draw_hp_bar(surf)






