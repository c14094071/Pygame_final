import pygame
from settings import *
import pygame
import time
import math
from towerView import TowerView
from enemy_type import Water as wt
from enemy_type import Stone as st
from enemy_type import DirtyWater as dw
from enemy_type import Badguy as bg
from enemy_type import DeadFish as df
from enemy_type import Boss01 as boss01
from enemy_type import Boss02 as boss02


class MainTower(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.water = 0

        self.puddle_index = 0
        self.image= pygame.transform.scale(pygame.image.load("images/puddle.png"), puddle_size[self.puddle_index])

        #self.base = pygame.Rect(0, 0, puddle_size[self.puddle_index][0], puddle_size[self.puddle_index][1])
        ##使用puddle size => 方便水池變大調整
        self.rect = self.image.get_rect()  ##這裡不用center=(x,y) 因為想以左上角為基準

        self.tower_fish = 100
        self.tower_max_fish = 100


    def update(self):
        pass

    def mainTower_bigger(self):
        pass
    def check_img2(self):
        self.image = pygame.transform.scale(pygame.image.load("images/puddle.png"), puddle_size[self.puddle_index])
        ##使用puddle size => 方便水池變大調整
        self.rect = self.image.get_rect()  ##這裡不用center=(x,y) 因為想以左上角為基準
    def check_img1(self):
        self.image = pygame.transform.scale(pygame.image.load("images/puddle2.png"), puddle_size2[self.puddle_index])

        ##使用puddle size => 方便水池變大調整
        self.rect = self.image.get_rect(center=((920-self.puddle_index*50),220))

    def check_water(self):
        if self.water>=2 and self.puddle_index<2:
            self.puddle_index +=1
            self.water = 0

    def draw(self, surf,stage):
        self.check_water()
        if stage ==0:
            self.check_img1()
        elif stage ==1:
            self.check_img2()


        surf.blit(self.image, self.rect)


class Tower(TowerView):
    def __init__(self, x, y,level, anim,damage, cost,
                 hp_list,max_hp_list,atk_list,range_list,cd_time_list):
        TowerView.__init__(self,x=x, y=y, anim=anim)

        self.hp_list = hp_list
        self.max_hp_list = max_hp_list
        self.atk_list = atk_list
        self.range_list = range_list
        self.cd_time_list = cd_time_list

        # self.x = x
        # self.y = y
        # self.anim = anim

        self.image = self.anim[0]
        #self.rect = self.image.get_rect(center=(x, y))
        #self.width = self.rect.width
        #self.height = self.rect.height

        # attack
        self.hp = self.hp_list[level-1]
        self.max_hp = self.max_hp_list[level-1]
        self.atk = self.atk_list[level-1]
        self.damage = damage
        self.att_range = self.range_list[level-1]
        self.cd_time = self.cd_time_list[level-1]  # Unit : seconds
        self.cost = cost

        self.drawcircle = False
        self.clicked = False

        self.last_cd = time.time() - 1
        ##animate

        self.animation_index = 0

        self.is_draw_range = False



    def is_cool_down(self):  ##回傳bool

        self.now = time.time()  ##取得現在的時間
        if self.now - self.last_cd >= self.cd_time:  ##現在的時間減掉上次使用的時間大於等於cd的話 就代表冷卻時間過了
            return False  ##冷卻已過
        else:
            return True  ##還在冷卻

    def is_in_range(self, enemy):  ##回傳bool

        if math.sqrt((enemy.x - self.x) ** 2 + (enemy.y - self.y) ** 2) <= self.att_range:  ##此塔的點與敵人的點之間的距離小於等於半徑
            return True  ##代表敵人在此塔的圓圈範圍內
        else:
            return False  ##範圍外

    # attack
    def update(self, enemy):  ##void
        from tower_type import Shovel as sh
        from tower_type import Pump as pp
        from tower_type import Goodguy as gg
        from tower_type import Cart as ct

        """
        detect the enemies in range and drop their health
        :param enemies: list
        :return: None
        """

        if not self.is_cool_down():  ##當冷卻已過
            for en in enemy:  ##對每個敵人做判斷
                if self.is_in_range(en):  ##如果有敵人在裡面
                    if isinstance(self, gg):
                        if isinstance(en, df):
                            en.hp -= self.atk  ##敵人就損血
                            self.last_cd = self.now  ##把使用攻擊的當下時間變成上次使用時間
                        else:
                            en.hp -= self.atk  ##敵人就損血
                            self.last_cd = self.now  ##把使用攻擊的當下時間變成上次使用時間
                        break
                    elif isinstance(self, pp):
                        # print(f"{self}/{en}")
                        if isinstance(en, wt):
                            en.hp -= self.atk  ##敵人就損血
                            self.last_cd = self.now  ##把使用攻擊的當下時間變成上次使用時間
                        if isinstance(en, boss01):
                            en.hp -= self.atk  ##敵人就損血
                            self.last_cd = self.now  ##把使用攻擊的當下時間變成上次使用時間
                        break
                    elif isinstance(self, sh):
                        # print(f"{self}/{en}")
                        if isinstance(en,st):
                            en.hp -= self.atk  ##敵人就損血
                            self.last_cd = self.now  ##把使用攻擊的當下時間變成上次使用時間
                        if isinstance(en, boss02):
                            en.hp -= self.atk  ##敵人就損血
                            self.last_cd = self.now  ##把使用攻擊的當下時間變成上次使用時間
                        break
                    elif isinstance(self, ct):
                        if isinstance(en,st):
                            en.hp -= self.atk  ##敵人就損血
                            self.last_cd = self.now  ##把使用攻擊的當下時間變成上次使用時間
                        if isinstance(en,df):
                            en.hp -= self.atk  ##敵人就損血
                            self.last_cd = self.now  ##把使用攻擊的當下時間變成上次使用時間
                        if isinstance(en, boss02):
                            en.hp -= self.atk  ##敵人就損血
                            self.last_cd = self.now  ##把使用攻擊的當下時間變成上次使用時間




    def is_clicked(self, x, y):  # 這裡的x, y將指到main.py裡滑鼠(游標)的位置

        '''
        if x >= (self.x - self.width / 2) and x <= (self.x + self.width / 2) and y >= (
                self.y - self.height / 2) and y <= (self.y + self.height / 2):
                '''
        if self.rect.collidepoint((x, y)):
            ##當滑鼠位置進入到塔的圖像範圍裡時
            if pygame.mouse.get_pressed()[
                0] == 1 and self.clicked == False:  ##滑鼠按下左鍵([0]==1) 且塔還沒按過(self.clicked = False)
                if self.drawcircle == False:  ##如果螢幕上此時沒有畫敵人塔的圓圈範圍
                    self.drawcircle = True  ##就畫圓圈圖像
                else:  ##如果螢幕上此時有畫敵人塔的圓圈範圍
                    self.drawcircle = False  ##則圓圈圖像就消失
                self.clicked = True  ##已經按了塔
            if pygame.mouse.get_pressed()[0] == 0:  ##當手放開左鍵
                self.clicked = False  ##狀態變回塔還沒按過
        '''
        self.clicked用來實現滑鼠單擊的效果 否則會出現使用者只按一下但被判定成pressedDown的狀況
        '''
        return self.drawcircle






    def draw(self, surf):
        # self.draw_tower(surf)
        self.animate(surf)
        self.draw_hp_bar(surf,self.hp,self.max_hp)
        pos = pygame.mouse.get_pos()  ##取得滑鼠位置
        # print(pos[0],pos[1],self.x,self.y)
        if self.is_clicked(pos[0], pos[1]):  ##是否要畫塔的圓圈範圍
            self.draw_range(surf)  ##畫圓圈範圍
