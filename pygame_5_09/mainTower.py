import pygame
from settings import *
import pygame
import time
import math
class MainTower(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.fish = 100
        self.salt = 0
        self.image = pygame.Surface((100,100))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect(center=(50,50))

    def update(self):
        pass
    def draw(self,surf):
        surf.blit(self.image,self.rect)
class Tower:
    def __init__(self):

        self.x = None
        self.y = None
        self.image = None
        self.rect = None
        self.width = None
        self.height = None

        self.hp = None
        self.max_hp = None
        self.atk = None
        self.drawcircle = False
        self.clicked = False
        # attack
        self.damage = 1
        self.att_range = 200
        self.cd_time = 1  # Unit : seconds
        self.last_cd = time.time() - 1

        self.is_draw_range = False

    def is_cool_down(self): ##回傳bool

        self.now = time.time()  ##取得現在的時間
        if self.now - self.last_cd >= self.cd_time:  ##現在的時間減掉上次使用的時間大於等於cd的話 就代表冷卻時間過了
            return False  ##冷卻已過
        else:
            return True  ##還在冷卻


    def is_in_range(self, enemy): ##回傳bool


        if math.sqrt((enemy.x - self.x) ** 2 + (enemy.y - self.y) ** 2) <= self.att_range:  ##此塔的點與敵人的點之間的距離小於等於半徑
            return True  ##代表敵人在此塔的圓圈範圍內
        else:
            return False  ##範圍外


    # attack
    def update(self, enemy): ##void
        """
        detect the enemies in range and drop their health
        :param enemies: list
        :return: None
        """

        if not self.is_cool_down():  ##當冷卻已過
            for en in enemy:  ##對每個敵人做判斷
                if self.is_in_range(en):  ##如果有敵人在裡面
                    en.hp -= self.damage  ##敵人就損血
                    self.last_cd = self.now  ##把使用攻擊的當下時間變成上次使用時間
                    # ---第2題---
                    # 請完成敵人扣血的機制
                    # 可以利用1.self.damage
                    break  # single attack (break會有單一攻擊的效果，可以試著拿掉看看會發生什麼事)

    def is_clicked(self, x, y):  # 這裡的x, y將指到main.py裡滑鼠(游標)的位置

        '''
        if x >= (self.x - self.width / 2) and x <= (self.x + self.width / 2) and y >= (
                self.y - self.height / 2) and y <= (self.y + self.height / 2):
                '''
        if self.rect.collidepoint((x,y)):
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

    def draw_range(self, surf):
        # ---第1題---
        # 請劃出塔的攻擊範圍，並且是以RGBA(有透明度)的圖案表示
        self.surface = pygame.Surface((self.att_range * 2, self.att_range * 2), pygame.SRCALPHA)  ##先畫在透明的畫布上
        self.circle = pygame.draw.circle(self.surface, (128, 128, 128, 100), (self.att_range, self.att_range),
                                         self.att_range)
        ##在畫布上畫圓
        surf.blit(self.surface, (self.x - self.att_range, self.y - self.att_range))  ##再把畫布(self.surface)放在視窗(surf)上

    def draw_tower(self, surf):
        surf.blit(self.image, (self.x - self.width // 2 + 8, self.y - self.height // 2))
    def draw_hp_bar(self, surf):

        if self.hp > 0:
            hp_width = self.width * (self.hp / self.max_hp)
            pygame.draw.rect(surf, RED_1, [self.x - self.width // 2, self.y + 55, self.width, 6], 0)
            pygame.draw.rect(surf, RED_2, [self.x - self.width // 2, self.y + 55, hp_width, 6], 0)
    def draw(self, surf):
        #self.draw_tower(surf)
        self.draw_hp_bar(surf)
        pos = pygame.mouse.get_pos()  ##取得滑鼠位置
        # print(pos[0],pos[1],self.x,self.y)
        if self.is_clicked(pos[0], pos[1]):  ##是否要畫塔的圓圈範圍
            self.draw_range(surf)  ##畫圓圈範圍


