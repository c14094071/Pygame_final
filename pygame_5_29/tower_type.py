from mainTower import *
import pygame


class Shovel(Tower):
    def __init__(self, x, y,level):
        Tower.__init__(self,x=x, y=y,level=level, anim=shovel_anim,
                       damage=5, cost=20,hp_list=shovel_hp_list,max_hp_list=shovel_max_hp_list,
                       atk_list=shovel_atk_list,range_list=shovel_range_list,cd_time_list=shovel_cd_time_list)



class Pump(Tower):
    # 在maintower的Tower完成數值
    def __init__(self, x, y,level):
        # 繼承tower
        Tower.__init__(self,x=x, y=y,level=level, anim=pump_anim,
                       damage=5, cost=20,hp_list=pump_hp_list,max_hp_list=pump_max_hp_list,
                       atk_list=pump_atk_list,range_list=pump_range_list,cd_time_list=pump_cd_time_list)



# 建立範圍攻擊塔
class Goodguy(Tower):
    def __init__(self, x, y,level):
        Tower.__init__(self,x=x, y=y,level=level, anim=goodguy_anim,
                       damage=5, cost=30,hp_list=goodguy_hp_list,max_hp_list=goodguy_max_hp_list,
                       atk_list=goodguy_atk_list,range_list=goodguy_range_list,cd_time_list=goodguy_cd_time_list)

class Cart(Tower):
    def __init__(self, x, y,level):
        Tower.__init__(self,x=x, y=y,level=level, anim=cart_anim,
                       damage=5, cost=10,hp_list=cart_hp_list,max_hp_list=cart_max_hp_list,
                       atk_list=cart_atk_list,range_list=cart_range_list,cd_time_list=cart_cd_time_list)


