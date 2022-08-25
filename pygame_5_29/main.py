import time

import pygame


from settings import *
from settings import towerposiList as tpl
from settings import PATH as path
from settings import towerPos_Coord as tpc
from settings import towerBtnList as tBL
import button
from mainTower import *

from button import *
from towerPos import *
from button import *
from enemy_generator import *
from tower_type import *
from Page import *
from enemy_type import Water as wt
from enemy_type import Boss01 as boss01
from enemy_type import Boss02 as boss02
from anima import Anima

# load image
game = None



# 真正判定主塔的圖片在mainTower.py

#font = pygame.font.SysFont("arialblack", 40)

class Music:
    def play_music_start(self):
        pygame.mixer.music.load("./bgm/startpage.mp3")
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(-1)
        # self.sound.set_volume(0.2)

    def play_music_game1(self):
        pygame.mixer.music.load("./bgm/game1.mp3")
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(-1)

    def play_music_game2(self):
        pygame.mixer.music.load("./bgm/game2.mp3")
        pygame.mixer.music.set_volume(1)
        pygame.mixer.music.play(-1)

    def play_music_losepage(self):
        pygame.mixer.music.load("./bgm/losepage.mp3")
        pygame.mixer.music.set_volume(0.6)
        pygame.mixer.music.play(-1)

    def play_music_winpage(self):
        pygame.mixer.music.load("./bgm/winpage.mp3")
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(-1)
class Create:
    def create_towerPos(self):  ##建立放塔的位置
        print("coord")
        for coord in towerPos_Coord:  ##塔的座標list

            # print(coord[0], coord[1])  ##x,y
            towerposi = TowerPosition(self.screen, coord[0], coord[1], 50, 40)  ##生成塔的位置
            towerposiList.append(towerposi)  ##把塔的位置的物件放入list

    def create_towerbutton_01(self):  ##建立塔的按鈕
        '''
        castnetbutton = CastnetButton(btnPos[0][0], btnPos[0][1], castnet_anim[0], 0.5, Castnet)
        towerBtnList.append(castnetbutton)
        '''
        goodguybutton = GoodguyButton(btnPos[0][0], btnPos[0][1], goodguy_anim[0], 0.5, Goodguy)
        towerBtnList.append(goodguybutton)
        pumpbutton = PumpButton(btnPos[1][0], btnPos[1][1], pump_anim[0], 0.5, Pump)
        towerBtnList.append(pumpbutton)


        self.upgradebutton1 = Upgradebutton(300, 460)
        self.upgradebutton2 = Upgradebutton(425, 460)
        self.upgradebutton3 = Upgradebutton(560, 460)
        self.breaktowerbtn = BreakTowerButton(775, 510)
        self.waterbutton = CleanWaterButton(900, 520)
class SwitchPage:
    def check_stage_two(self):
        if self.wave == 3:
            self.stage = 1
            self.bg = background_image2
            pygame.mixer.music.pause()
            self.play_music_game2()
    def check_thestage(self):
        if self.stage == 0:
            self.thestage = "Stage : " + str(self.stage + 1) + " , Wave : " + str(self.wave + 1)
        if self.stage == 1:
            self.thestage = "Stage : " + str(self.stage + 1) + " , Wave : " + str(self.wave - 2)

    def switchToStage2(self):
        self.pageBetween1and2()
        path.clear()
        tpl.clear()
        tpc.clear()
        path[:] = PATH2[:]
        tpc[:] = towerPos_Coord2[:]
        tBL.pop()
        shovelbutton = ShovelButton(btnPos[1][0], btnPos[1][1], shovel_anim[0], 0.5, Shovel)
        towerBtnList.append(shovelbutton)
        cartbutton = CartButton(btnPos[2][0], btnPos[2][1], cart_anim[0], 0.5, Cart)
        towerBtnList.append(cartbutton)
        self.create_towerPos()


    def pageBetween1and2(self):
        pagecount = 0
        go_button = Button(WIN_WIDTH - 70, WIN_HEIGHT - 535, go_image)
        next = False
        while True:
            self.clock.tick(FPS)
            self.screen.blit(next_image[pagecount], (0, 0))
            if pagecount ==1:
                go_button.draw(self.screen)

            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.show_endingPage = False
                    self.running = False
                    next = True
                if event.type == pygame.MOUSEBUTTONUP:
                    pagecount +=1
                    if pagecount ==2:
                        next = True
            if next:
                break


    def draw_startPage(self):  ##開始畫面
        if self.show_startPage == False:
            return

        waiting = True

        start_button = Button(WIN_WIDTH / 2, WIN_HEIGHT / 2 + 40, start_img)
        quit_button = Button(WIN_WIDTH / 2, WIN_HEIGHT / 2 + 120, quit_img)

        while waiting:
            self.clock.tick(FPS)  ## 1秒只能做60次迴圈
            self.screen.blit(startPage_img, (0, 0))
            ##建立按鈕
            if start_button.draw(self.screen):
                waiting = False
            if quit_button.draw(self.screen):
                self.running = False
                self.show_betwSGPage = False
                waiting = False
            # 取得輸入

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # pygame.quit() =>會導致不正常關閉遊戲
                    self.running = False
                    self.show_betwSGPage = False
                    waiting = False
            pygame.display.update()

    def betweenStart_and_Game(self):
        if self.show_betwSGPage == False:
            return
        waiting = True
        #####龍捲風&老人動畫#####
        tornado_anim = [pygame.transform.scale(pygame.image.load(os.path.join(f"images/tornado/tornado-{i}.png")), (200, 200)) for i
            in range(16)]
        walkingman_anim = [pygame.transform.scale(pygame.image.load(os.path.join(f"images/walking man/walking_man_{i}.png")),
                                   (180, 180)) for i in range(10)]

        betwSG_count = 0
        nextpage_button = Button(WIN_WIDTH - 70, WIN_HEIGHT - 535, nextpage_image)
        self.wkingman = Anima(600,280,walkingman_anim)
        self.tona = Anima(800,215,tornado_anim)


        betwSG_image = [pygame.image.load(f"images/BETWEENPAGE/start_page_{i}.jpg") for i in range(5)]
        betwSG_image1 = betwSG_image[0]
        oo = False
        while waiting:
            self.clock.tick(FPS)  ## 1秒只能做60次迴圈

            self.screen.blit(betwSG_image1, (0, 0))
            #print(betwSG_count)
            ##建立按鈕
            if betwSG_count ==0:
                self.wkingman.animate(self.screen)
            if betwSG_count ==1:
                self.tona.animate(self.screen)
                pass
            if betwSG_count ==4:
                nextpage_button.image = go_image


            if betwSG_count <= 3 and nextpage_button.draw(self.screen):
                betwSG_count += 1
                betwSG_image1 = betwSG_image[betwSG_count]
            elif betwSG_count == 4 and nextpage_button.draw(self.screen):
                break


            '''
            if betwSG_count <= 2 and nextpage_button.draw(self.screen):
                betwSG_count += 1
                betwSG_image1 = betwSG_image[betwSG_count]
                print("@@@")
            elif betwSG_count == 3 and go_button.draw(self.screen):

                break
            '''

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # pygame.quit() =>會導致不正常關閉遊戲
                    self.running = False
                    waiting = False
            pygame.display.update()


##主遊戲
class Game(Music,Create,SwitchPage):
    def __init__(self):
        self.running = True
        self.clock = pygame.time.Clock()
        self.start_time = None
        self.bg = background_image1
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))  ##建立視窗
        pygame.display.set_caption("魚")
        self.font_size = 30  # 字體大小
        self.font = pygame.font.Font("New-Super-Mario-Font-U-1.ttf", self.font_size)
        self.font01 = pygame.font.Font("New-Super-Mario-Font-U-1.ttf", 25)

        self.show_startPage = True  ##開始畫面boolean
        self.show_betwSGPage = True
        self.show_endingPage = True

        self.create_towerPosBool = True  ##建立塔的位置boolean
        self.create_towerBtnBool = True  ##建立塔的按鈕boolean
        # self.all_sprites = pygame.sprite.Group()  ##建立sprite群組->先把要畫的東西聚集在一起
        self.main_tower = MainTower()  ##生成主塔

        # self.all_sprites.add(self.main_tower) ##放入主塔

        ##載入按鈕圖片

        ##敵人波
        self.is_next_wave = False
        self.wave = 0
        self.stage = 0
        self.thestage = "Stage : " + str(self.stage + 1) + " , Wave : " + str(self.wave + 1)
        self.enemies = []
        self.towers = []
        self.extra_money = 0
        self.now_money = 0
        self.game_time = 0
        self.enemy_generator = EnemyGenerator()
        ##第二關
        self.switch2 = True
        ##BOSS
        self.Boss01_born = True
        self.Boss02_born = True

        ##勝利
        self.win = False




    def upgrade_got_click(self, x: int, y: int):
        if self.upgradebutton1.clicked(x, y) and towerBtnList[0].buttonlevel <= 4 and self.now_money > 40:
            towerBtnList[0].buttonlevel += 1
            self.extra_money -= 40


        if self.upgradebutton2.clicked(x, y) and towerBtnList[1].buttonlevel <= 4 and self.now_money > 25:
            towerBtnList[1].buttonlevel += 1
            self.extra_money -= 25
        if len(towerBtnList) ==3 and self.upgradebutton3.clicked(x, y) and towerBtnList[2].buttonlevel <= 4 and self.now_money > 20:
            towerBtnList[2].buttonlevel += 1
            self.extra_money -= 20

    def draw_cost(self):
        pos = pygame.mouse.get_pos()
        if self.upgradebutton1.rect.collidepoint(pos):
            money40_text = self.font01.render("$40", True, upgrade_color)
            self.screen.blit(money40_text, self.upgradebutton1.rect.midright)
        if self.upgradebutton2.rect.collidepoint(pos):
            money25_text = self.font01.render("$25", True, upgrade_color)
            self.screen.blit(money25_text, self.upgradebutton2.rect.midright)
        if self.upgradebutton3.rect.collidepoint(pos):
            money20_text = self.font01.render("$20", True, upgrade_color)
            self.screen.blit(money20_text, self.upgradebutton3.rect.midright)
        if towerBtnList[0].rect.collidepoint(pos):
            money30_text = self.font01.render("$30",True,buy_tower_color)
            self.screen.blit(money30_text,towerBtnList[0].rect.bottomleft)
        if towerBtnList[1].rect.collidepoint(pos):
            money20_text = self.font01.render("$20",True,buy_tower_color)
            self.screen.blit(money20_text,towerBtnList[1].rect.bottomleft)
        if len(towerBtnList)==3 and towerBtnList[2].rect.collidepoint(pos):
            money10_text = self.font01.render("$10",True,buy_tower_color)
            self.screen.blit(money10_text,towerBtnList[2].rect.bottomleft)



    def show_water(self, surf):
        the_water = "water : " + str(self.main_tower.water)
        # pygame.draw.rect(surf, BLACK, [162, 0, 150, 40])  # 計時器黑框
        my_text = self.font.render(the_water, True, WHITE)  # 計時器白字
        surf.blit(my_text, (170, 5))

    def show_stage(self, surf):
        # pygame.draw.rect(surf, BLACK, [362, 0, 300, 40])  # 計時器黑框
        my_text = self.font.render(self.thestage, True, WHITE)  # 計時器白字
        surf.blit(my_text, (380, 5))
        pass

    def count_money(self, surf):
        now_time = time.time()
        self.game_time = int(now_time - self.start_time)
        self.now_money = str(self.game_time * 5 + self.extra_money)
        self.now_money = "money : " + self.now_money
        # pygame.draw.rect(surf, BLACK, [834, 0, 190, 40])  # 計時器黑框
        my_text = self.font.render(self.now_money, True, WHITE)  # 計時器白字
        surf.blit(my_text, (33, 520))
        self.now_money = self.game_time * 5 + self.extra_money
        pass

    def next_wave(self):
        # 按下鍵盤中'n'按鈕後(self.is_next_wave=True)能夠產生一波敵人的動作
        # 並且敵人隨著波數的增加，會提高血量、出怪量...等
        # 最多可以有?波的敵人
        if self.is_next_wave == True and self.wave < 8:
            self.enemy_generator.generate(self.enemies, self.wave, self.stage)
            if self.wave == 2 and self.Boss01_born and self.enemy_generator.enemy_nums[self.wave] == 0:
                self.enemies.append(Boss01())
                self.Boss01_born = False
            if self.wave == 7 and self.Boss02_born and self.enemy_generator.enemy_nums[self.wave] == 0:
                self.enemies.append(Boss02())
                self.Boss02_born = False
            # self.change_PATH2()
            if self.enemy_generator.enemy_nums[self.wave] == 0:
                self.wave += 1
                self.is_next_wave = False



    def update(self):
        self.breaktowerbtn.breaktower()
        self.clean_wa()
        self.next_wave()
        for en in self.enemies:
            en.update(self.towers)
            #print(en.hp)

        for tp in towerposiList:
            if tp.towerType:
                tp.towerType.update(self.enemies)



    def draw_base_hp(self):  # 畫主塔血量條
        if self.main_tower and self.stage == 1:
            base_hp_height = 100 * (self.main_tower.tower_fish / self.main_tower.tower_max_fish)
            pygame.draw.rect(self.screen, PUR_1, [65, 220, 100, 15], 0)
            pygame.draw.rect(self.screen, PUR_2, [65 + (100 - base_hp_height), 220, base_hp_height, 15], 0)
        elif self.main_tower and self.stage == 0:
            base_hp_height = 100 * (self.main_tower.tower_fish / self.main_tower.tower_max_fish)
            pygame.draw.rect(self.screen, PUR_1, [865, 300, 100, 15], 0)
            pygame.draw.rect(self.screen, PUR_2, [865 + (100 - base_hp_height), 300, base_hp_height, 15], 0)

    def draw(self, surf):  ##繪畫塔和敵人
        surf.blit(self.bg, (0, 0))
        self.count_money(surf)
        self.show_stage(surf)
        self.show_water(surf)

        for tb in towerBtnList:  ##畫按鈕
            tb.draw(self.now_money, self.screen)
            # tb.draw(self.screen)
        self.upgradebutton1.draw(surf)
        self.upgradebutton2.draw(surf)
        if len(towerBtnList)==3:
            self.upgradebutton3.draw(surf)
        self.breaktowerbtn.draw(surf)
        self.waterbutton.draw(surf)

        # print(self.enemies)

        for tp in towerposiList:  ##畫坑
            tp.draw(self.screen)

        for en in self.enemies:  ##畫敵人
            en.draw(self.screen)
        self.draw_cost()
        self.main_tower.draw(self.screen, self.stage)  ##畫主塔
        if self.stage == 1:
            self.screen.blit(fishpool_img, (0, 0))  ##畫魚塭(單純繪圖上去，無實質作用) NOTICE: 這一定要放最後畫
        elif self.stage == 0:
            self.screen.blit(fishpool_img2, (800, 100))
        self.draw_base_hp()  ##一樣最後 才不會被蓋到


    ###############
    def clean_wa(self):
        if self.waterbutton.clicked() == True and self.main_tower.puddle_index > 0 and self.now_money >= 50:
            self.main_tower.puddle_index -= 1
            self.extra_money -= 50

    def game_operation(self):
        if self.main_tower:
            for en in self.enemies:
                if self.main_tower.rect.collidepoint((en.x, en.y)) and en in self.enemies:
                    self.enemies.remove(en)
                    if isinstance(en, wt):  ##判斷前面的是否屬於後面的class
                        self.main_tower.water += 1
                    else:
                        self.main_tower.tower_fish -= en.atk * 3
                    if isinstance(en, boss01):
                        self.main_tower.tower_fish -= 50
                        self.main_tower.tower_fish += en.atk * 3
                    if isinstance(en, boss02):
                        self.main_tower.tower_fish -= 100
                        self.main_tower.tower_fish += en.atk * 3
                if en in self.enemies and en.hp <= 0:
                    self.enemies.remove(en)
                    self.extra_money += en.money

        if self.main_tower.tower_fish <= 0:
            pygame.mixer.music.pause()
            self.play_music_losepage()
            self.running = False
            self.win = False



    #####遊戲畫面######
    def game_run(self):
        restart = False
        path.clear()
        tpl.clear()
        tpc.clear()
        tBL.clear()
        tpc[:] = towerPos_Coord1[:]
        path[:] = PATH1[:]
        self.__init__()

        ##開始畫面
        ##顯示開始畫面
        self.play_music_start()
        self.draw_startPage()
        self.betweenStart_and_Game()

        if self.running == False:
            self.show_endingPage = False
        pygame.mixer.music.pause()
        self.play_music_game1()

        self.start_time = time.time()
        ###遊戲中內容
        while self.running:
            self.clock.tick(FPS)
            ##建立塔的位置和按鈕
            if self.create_towerPosBool:
                self.create_towerPos()
                self.create_towerPosBool = False
            if self.create_towerBtnBool:
                self.create_towerbutton_01()
                self.create_towerBtnBool = False
            ##################

            if self.running == False:  ##開始畫面按下Quit後，running->False，後面的遊戲畫面就不顯示
                continue
            ##Victor
            mouse_x, mouse_y = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.show_endingPage = False
                    self.running = False

                if event.type == pygame.MOUSEBUTTONUP:
                    pass
                ##Victor
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.upgrade_got_click(mouse_x, mouse_y)
                    # 設定當按下鍵盤'n'時，可以有一波的敵人
                if event.type ==pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        for tp in towerposiList:
                            if tp.focus == True:
                                add = towerBtnList[0].put_towerType_gg(tp)

                                if self.now_money - add < 0:
                                    add = 0
                                    tp.towerType = None
                                else:
                                    self.extra_money -= add
                                    tp.towerlevel = towerBtnList[0].buttonlevel
                                    tp.focus = False
                        pass

                    if event.key == pygame.K_s:
                        for tp in towerposiList:
                            if tp.focus == True:
                                if self.stage ==0:
                                    add = towerBtnList[1].put_towerType_pp(tp)
                                elif self.stage ==1:
                                    add = towerBtnList[1].put_towerType_sh(tp)


                                if self.now_money - add < 0:
                                    add = 0
                                    tp.towerType = None
                                else:
                                    self.extra_money -= add
                                    tp.towerlevel = towerBtnList[1].buttonlevel
                                    tp.focus = False
                        pass
                    if len(towerBtnList)== 3 and event.key == pygame.K_d:
                        for tp in towerposiList:
                            if tp.focus == True:
                                add = towerBtnList[2].put_towerType_ct(tp)
                                if self.now_money - add < 0:
                                    add = 0
                                    tp.towerType = None
                                else:
                                    self.extra_money -= add
                                    tp.towerlevel = towerBtnList[2].buttonlevel
                                    tp.focus = False
                        pass


            if self.game_time == 0 and self.stage == 0:
                self.is_next_wave = True
            elif self.stage == 0:
                if self.game_time > 25 * (self.wave):
                    if self.wave < 3:
                        self.check_stage_two()
                        self.check_thestage()
                        self.is_next_wave = True

                    if self.wave == 3 and len(self.enemies) == 0:
                        self.extra_money += self.game_time * 5
                        self.check_stage_two()
                        self.check_thestage()
                        self.is_next_wave = True
                        if self.switch2 == True:
                            self.switchToStage2()
                            self.start_time = time.time()
                            self.switch2 = False

            elif self.stage == 1:
                if self.game_time > 25 * (self.wave-3):
                    self.check_thestage()
                    self.is_next_wave = True

            # self.all_sprites.update()
            self.game_operation()

            # self.screen.fill((255, 255, 255))

            # self.all_sprites.draw(self.screen)
            self.draw(self.screen)

            self.update()

            if self.wave == 8 and len(self.enemies) == 0 and self.main_tower.tower_fish>0:
                self.running = False
                self.win = True


            pygame.display.update()

        ###遊戲結束畫面
        if self.show_endingPage and self.win == False:
            pygame.mixer.music.pause()
            self.play_music_losepage()
            restart = lose_page(self.screen, self.clock)

        elif self.show_endingPage and self.win == True:
            pygame.mixer.music.pause()
            self.play_music_winpage()
            restart = win_page(self.screen, self.clock)
        if restart == True:
            self.game_run()

        pygame.quit()




if __name__ == "__main__":
    pygame.init()
    game = Game()
    game.game_run()
