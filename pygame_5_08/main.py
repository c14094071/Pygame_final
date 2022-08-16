import pygame
from settings import *
import button
from mainTower import *

from button import *
from towerPos import *
from button import *
from enemy_generator import *
from tower_type import *

pygame.init()

font = pygame.font.SysFont("arialblack", 40)

'''
def draw_text(screen,text,font,text_col,x,y):
    img = font.render(text,True,text_col)
    screen.blit(img,(x,y))
'''


##主遊戲
class Game:
    def __init__(self):
        self.running = True
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))  ##建立視窗
        pygame.display.set_caption("魚")

        self.show_startPage = True  ##開始畫面boolean

        self.create_towerPosBool = True  ##建立塔的位置boolean
        self.create_towerBtnBool = True  ##建立塔的按鈕boolean
        # self.all_sprites = pygame.sprite.Group()  ##建立sprite群組->先把要畫的東西聚集在一起
        self.main_tower = MainTower()  ##生成主塔
        self.base = pygame.Rect(0,0,100,100)
        self.tower_fish = 100
        self.tower_max_fish= 100
        # self.all_sprites.add(self.main_tower) ##放入主塔

        ##載入按鈕和畫面圖片
        self.starPage_img = pygame.image.load("images/startPage.jpg")
        self.background_img = pygame.image.load("images/background.jpg")

        self.start_img = pygame.image.load("images/start.png").convert_alpha()
        self.quit_img = pygame.image.load("images/quit.png").convert_alpha()
        self.castnetBtn_img = pygame.image.load(tower01_img).convert_alpha()
        self.goodguy_img = pygame.image.load("images/goodguybutton_img.jpg").convert_alpha()
        self.pumpbutton_img = pygame.image.load("images/pumpbutton_img.jpg").convert_alpha()
        ##建立按鈕
        self.start_button = Button(WIN_WIDTH / 2, WIN_HEIGHT / 2 +40 , self.start_img, 0.3,0.1)
        self.quit_button = Button(WIN_WIDTH / 2 , WIN_HEIGHT / 2 +120, self.quit_img, 0.3,0.1)
        ##敵人波
        self.is_next_wave = False
        self.wave = 0
        self.enemies = []
        self.towers = []
        self.enemy_generator = EnemyGenerator()
        ##建立按鈕


    def next_wave(self):

        # 按下鍵盤中'n'按鈕後(self.is_next_wave=True)能夠產生一波敵人的動作
        # 並且敵人隨著波數的增加，會提高血量、出怪量...等
        # 最多可以有5波的敵人
        if self.is_next_wave == True and self.wave < 5:
            self.enemy_generator.generate(self.enemies, self.wave)
            if self.enemy_generator.enemy_nums[self.wave] == 0:
                self.wave += 1
                self.is_next_wave = False

    def create_towerPos(self):  ##建立放塔的位置

        for coord in towerPos_Coord:  ##塔的座標list
            #print(coord[0], coord[1])  ##x,y
            towerposi = TowerPosition(self.screen, coord[0], coord[1], 50, 40)  ##生成塔的位置
            towerposiList.append(towerposi)  ##把塔的位置的物件放入list

    def create_towerbutton(self): ##建立塔的按鈕

        castnetbutton = CastnetButton(300, 500, self.castnetBtn_img, 0.5,Castnet)
        towerBtnList.append(castnetbutton)
        pumpbutton = PumpButton(500, 500, self.pumpbutton_img, 0.5,Pump)
        towerBtnList.append(pumpbutton)
        goodguybutton = GoodguyButton(700, 500, self.goodguy_img, 0.5,Goodguy)
        towerBtnList.append(goodguybutton)

    def draw_tower(self):

        pass

    def update(self):
        self.next_wave()
        for en in self.enemies:
            en.update(self.towers)

        for tp in towerposiList:
            if tp.towerType:
                tp.towerType.update(self.enemies)

    def draw_base_hp(self):  # 畫主塔血量條
        base_hp_height = 100 * (self.tower_fish / self.tower_max_fish)
        pygame.draw.rect(self.screen, RED_1, [110, 30, 10, 100], 0)
        pygame.draw.rect(self.screen, RED_2, [110, 30 + (100 - base_hp_height), 10, base_hp_height], 0)

    def draw(self): ##繪畫塔和敵人
        self.draw_base_hp()
        for tow in towerposiList:
            tow.draw(self.screen)
        for en in self.enemies:
            en.draw(self.screen)


    def draw_startPage(self):  ##開始畫面
        pygame.display.update()
        self.waiting = True

        while self.waiting:
            self.clock.tick(FPS)  ## 1秒只能做60次迴圈
            self.screen.blit(self.starPage_img,(0,0))
            if self.start_button.draw(self.screen):
                self.waiting = False

            if self.quit_button.draw(self.screen):
                self.running = False
                self.waiting = False
            # 取得輸入

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # pygame.quit() =>會導致不正常關閉遊戲
                    self.running = False
                    self.waiting = False
            pygame.display.update()

    ###############
    def game_operation(self):
        for en in self.enemies:
            if self.base[0] < en.x < self.base[0] + self.base[2] and self.base[1] < en.y < self.base[1] + self.base[3]:
                self.enemies.remove(en)
                self.tower_fish -= 5
            if en.hp <= 0:
                self.enemies.remove(en)
                #self.money += 20

        if self.tower_fish <= 0:
            self.running = False
    #####遊戲畫面######
    def game_run(self):

        while self.running:

            if self.show_startPage:  ##顯示開始畫面
                self.draw_startPage()
                self.show_startPage = False
            self.clock.tick(FPS)
            ##建立塔的位置和按鈕
            if self.create_towerPosBool:
                self.create_towerPos()
                self.create_towerPosBool = False
            if self.create_towerBtnBool:
                self.create_towerbutton()
                self.create_towerBtnBool = False
            ##################

            if self.running == False:  ##開始畫面按下Quit後，running->False，後面的遊戲畫面就不顯示
                continue
            self.game_operation()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONUP:
                    pass
                    # 設定當按下鍵盤'n'時，可以有一波的敵人
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_n:
                        self.is_next_wave = True

            # self.all_sprites.update()
            self.update()

            self.screen.blit(self.background_img,(0,0))

            # self.all_sprites.draw(self.screen)
            self.draw()

            self.main_tower.draw(self.screen)
            for tb in towerBtnList:
                tb.draw(self.screen)

            pygame.display.update()


if __name__ == "__main__":
    game = Game()
    game.game_run()
