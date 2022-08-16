import pygame
import time

from enemy_type import *



class EnemyGenerator:
    def __init__(self):

        # 敵人波數設置
        self.enemy_nums = [3, 6, 9, 12, 15]
        self.enemy_max_hp = [8, 10, 12, 14, 16]
        self.gen_enemy_time = time.time()
        self.gen_period = [2, 0.5, 0.3, 0.3, 0.2]

    def generate(self, enemy, wave):
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
            enemy.append(Water(self.enemy_max_hp[wave]))
