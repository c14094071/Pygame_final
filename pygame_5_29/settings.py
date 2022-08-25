import pygame
import os
'''
注意!!
不可使用 .conver_alpha()
例如quit_img = pygame.image.load("images/quit.png").convert_alpha()
因為視窗還沒setmode 所以會報錯 
'''
buy_tower_color= (61,89,171)
upgrade_color =(178,34,34)
FPS = 60
WHITE = (255,255,255)
BLUE = (0,0,255)
RED_1 = "#F9C0C4"
RED_2 = "#FA3C39"
PUR_1 = "#E6CAFF"
PUR_2 = "#6F00D2"
WIN_WIDTH = 1024
WIN_HEIGHT = 600
GREEN = (0,255,0)
BLACK = (0,0,0)
towerPos_Coord=[]
towerPos_Coord1 = [(129, 208), (219, 184), (232, 330), (315, 228),
(307, 367), (402, 269), (547, 380), (501, 245), (596, 194), (648, 389),
(723, 254), (863, 396), (831, 239), (964, 335), (987, 227), (96, 394)]
towerPos_Coord2 = [(402, 182), (328, 324), (78, 363),
(451, 323), (550, 327), (634, 330), (852, 325), (939, 322),
(533, 254), (563, 100), (396, 69), (194, 239), (266, 190), (101, 281)]


towerposiList = [] ##可以放塔的位置物件list
towerBtnList = []
PATH=[]
PATH1 = [(6, 355), (29, 354), (55, 354), (78, 346), (101, 335),
         (117, 328), (134, 314), (151, 300), (168, 284), (190, 269),
         (212, 264), (235, 263), (262, 274), (278, 287), (294, 301),
         (314, 315), (339, 327), (363, 336), (387, 348), (419, 353),
         (447, 354), (477, 343), (503, 328), (528, 311), (555, 295),
         (582, 281), (616, 285), (639, 302), (661, 313), (681, 325),
         (701, 337), (721, 345), (744, 347), (768, 349), (800, 344),
         (830, 328), (856, 318), (879, 302), (899, 277), (914, 255),
         (923, 232), (927, 201)]
PATH2 = [(1019, 391), (998, 391), (978, 392), (949, 391),
(919, 391), (900, 389), (872, 392), (848, 393), (810, 389),
(782, 390), (753, 389), (723, 390), (698, 387), (670, 387),
(635, 388), (609, 387), (579, 387), (547, 386), (515, 389),
(479, 383), (450, 383), (417, 383), (391, 379), (359, 380),
(324, 378), (296, 375), (269, 375), (240, 370), (216, 356),
(198, 347), (202, 333), (215, 319), (237, 307), (263, 296),
(287, 283), (310, 274), (342, 265), (369, 254), (388, 243),
(414, 230), (434, 219), (459, 209), (482, 201), (500, 183),
(502, 160), (483, 151), (462, 145), (436, 138), (405, 138),
(377, 133), (347, 128), (324, 125), (292, 126), (267, 124),
(246, 123), (224, 121), (189, 117), (161, 112)]



tower01_img = "images/tower01.png"
enemy_hpbar = 10
puddle_size2 = [(200,200),(300,300),(400,400)]
puddle_size = [(200,150),(300,200),(400,280)]

#####畫面######
startPage_img = pygame.image.load("images/startPage.jpg")
background_image1 = pygame.transform.scale(pygame.image.load("images/background new_1.jpg"), (WIN_WIDTH, WIN_HEIGHT))
background_image2 = pygame.transform.scale(pygame.image.load("images/background new_2.jpg"), (WIN_WIDTH, WIN_HEIGHT))
fishpool_img = pygame.transform.scale(pygame.image.load("images/Fish pool.png"),(200,200)) ##單純繪畫魚塭 無用處
fishpool_img2 = pygame.transform.scale(pygame.image.load("images/Fish pool_2.png"),(200,200)) ##單純繪畫魚塭 無用處

#####塔的動畫###
shovel_anim = [pygame.transform.scale(pygame.image.load(f"images/shovel/shovel-{i}.png"),(60,60)) for i in range(22)]
pump_anim = [pygame.transform.scale(pygame.image.load(f"images/pumps/pump-{i}.png"), (60, 60)) for i in range(4)]
goodguy_anim = [pygame.transform.scale(pygame.image.load(f"images/goodguys/[attackbat -_00001] (imported)-attackbat -_000{i}.png.png"),(60,60)) for i in range(14)]
castnet_anim = [pygame.transform.scale(pygame.image.load(f"images/castnets/castnet-{i}.png"),(60,60)) for i in range(9)]
cart_anim = [pygame.transform.scale(pygame.image.load(f"images/cart/cart-{i}.png"),(50,50)) for i in range(21)]

#####按鈕#####

start_img = pygame.transform.scale(pygame.image.load("images/start.png"),(265,88))
quit_img = pygame.transform.scale(pygame.image.load("images/quit.png"),(183,61))




#####塔數值####
shovel_hp_list = [30, 35, 45, 50, 55]
shovel_max_hp_list = [30, 35, 45, 50, 55]
shovel_atk_list = [1, 2, 3, 4, 4]
shovel_range_list = [100, 100, 100, 150, 150]
shovel_cd_time_list = [1, 0.8, 0.6, 0.6, 0.5]

cart_hp_list = [10, 15, 20, 25, 30]
cart_max_hp_list = [10, 15, 20, 25, 30]
cart_atk_list = [4, 4, 5, 7, 8]
cart_range_list = [150, 150, 150, 200, 225]
cart_cd_time_list = [1, 0.8, 0.7, 0.6, 0.6]

pump_hp_list = [30, 35, 35, 35, 40]
pump_max_hp_list = [30, 35, 35, 35, 40]
pump_atk_list = [5, 5, 8, 10, 10]
pump_range_list = [100, 100, 150, 150, 150]
pump_cd_time_list = [1.2, 1, 1, 0.8, 0.8]

goodguy_hp_list = [20, 20, 30, 30, 30]
goodguy_max_hp_list = [20, 20, 30, 30, 30]
goodguy_atk_list = [2, 4, 5, 7, 7]
goodguy_range_list = [200, 250, 250, 250, 350]
goodguy_cd_time_list = [2, 1.5, 1.2, 1.1, 1]
#####敵人數值####
water_hp_list = [10, 0]
water_max_hp_list = [10, 0]
water_atk_list = [1, 0]
water_range_list = [100, 0]
water_cd_time_list = [0.8, 0]

dirtywater_hp_list = [15, 0]
dirtywater_max_hp_list = [15, 0]
dirtywater_atk_list = [3, 0]
dirtywater_range_list = [100, 0]
dirtywater_cd_time_list = [1, 0]

badguy_hp_list = [0, 80]
badguy_max_hp_list = [0, 80]
badguy_atk_list = [0, 5]
badguy_range_list = [0, 150]
badguy_cd_time_list = [0, 0.7]

deadfish_hp_list = [0, 20]
deadfish_max_hp_list = [0, 20]
deadfish_atk_list = [0, 8]
deadfish_range_list = [0, 200]
deadfish_cd_time_list = [0, 0.5]

stone_hp_list = [0, 70]
stone_max_hp_list = [0, 70]
stone_atk_list = [0, 2]
stone_range_list = [0, 100]
stone_cd_time_list = [0, 0.9]

#####敵人動畫#####
water_anim = [pygame.transform.scale(pygame.image.load(os.path.join(f"images/water/water-{i}.png")), (60, 60)) for i in range(12)]
badguy_anim =[pygame.transform.scale(pygame.image.load(os.path.join(f"images/thief/thief{i}.png")), (60, 60)) for i in range(13)]
dirtywater_anim = [pygame.transform.scale(pygame.image.load(os.path.join(f"images/dirtywater/dirtywater-{i}.png")),(60,60)) for i in range(13)]
deadfish_anim = [pygame.transform.scale(pygame.image.load(os.path.join(f"images/deadfish/deadfish-{i}.png")),(60,60)) for i in range(8)]
stone_anim = [pygame.transform.scale(pygame.image.load(os.path.join(f"images/stone/stone-{i}.png")),(60,60)) for i in range(32)]

#####關卡#####
STAGE = 0

#載入下一頁按鈕
nextpage_image = pygame.transform.scale(pygame.image.load("images/nextpage.png"),(75,75))
go_image = pygame.transform.scale(pygame.image.load("images/GO.png"), (75,75))
exit_image = pygame.transform.scale(pygame.image.load(f"images/EXIT.png"),(75,75))
restart_image = pygame.transform.scale(pygame.image.load(f"images/restart.png"),(75,75))
#載入過關畫面
next_image = [pygame.image.load(f"images/ENDING/換關畫面{i}.jpg") for i in range(2)]
#載入過關畫面
#win_image = pygame.image.load("images/ENDING/WIN Ending.jpg")

##BOSS動畫###
boss02_anim = [pygame.transform.scale(pygame.image.load(os.path.join(f"images/Boss_01/987787e218d5d367152ed52d5c7bccd2-{i}-removebg-preview.png")),(200,200)) for i in range(16)]
#boss02_anim = [pygame.transform.scale(pygame.image.load(os.path.join(f"images/typhoon01/BigCircularBabirusa-max-1mb-{i}.png")),(200,200)) for i in range(30)]
boss01_anim = [pygame.transform.scale(pygame.image.load(os.path.join(f"images/typhoon02/top-faridabad-tornado-stickers-for-android-ios-gfycat-{i+1}.png")),(200,200)) for i in range(29)]

##按鈕位置
btnPos = [(260, 520),(380, 520),(522, 520)]

