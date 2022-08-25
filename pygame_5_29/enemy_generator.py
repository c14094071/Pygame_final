import pygame
import time
import random

from enemy_type import *



class EnemyGenerator:
    def __init__(self):

        # 敵人波數設置
        self.enemy_nums = [3, 4, 6, 5, 8, 8, 15, 3]
        self.gen_enemy_time = time.time()
        self.gen_period = [2, 1, 0.8, 1, 1.2, 0.6, 0.7, 1]

    def generate(self, enemy, wave,stage):
        """
        generate the enemy to the enemy list according to the given wave
        :param enemies: list
        :param wave: int
        :return: None
        """

        now = time.time()
        if now - self.gen_enemy_time >= self.gen_period[wave] and self.enemy_nums[wave] > 0:  # wave interval
            self.gen_enemy_time = now
            self.enemy_nums[wave] -= 1
            if wave ==0:
                enemygen = random.choices([Water(stage), Water(stage)], weights=[70, 30])
            elif  wave <=2:
                enemygen = random.choices([Water(stage),DirtyWater(stage)], weights=[40, 60])
            elif wave>2:
                enemygen = random.choices([Stone(stage), DeadFish(stage), Badguy(stage)], weights=[55, 30, 15])
            enemy.append(enemygen[0])


