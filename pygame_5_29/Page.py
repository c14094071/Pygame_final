import pygame
from settings import *
from button import *



def lose_page(surf, clock):
    restart = False
    waiting = True
    losepage_count = 0
    nextpage_button = Button(WIN_WIDTH - 70, WIN_HEIGHT - 535, nextpage_image)
    restart_button = Button(WIN_WIDTH -160, WIN_HEIGHT-535, restart_image)

    lose_image = [pygame.image.load(f"images/ENDING/LOSE ending _{i}.jpg") for i in range(5)]
    lose_image1 = lose_image[0]
    while waiting:
        clock.tick(FPS)  ## 1秒只能做60次迴圈
        surf.blit(lose_image1, (0, 0))
        ##建立按鈕

        if losepage_count == 4:
            nextpage_button.image = exit_image
        if losepage_count <= 3 and nextpage_button.draw(surf):
            losepage_count += 1
            lose_image1 = lose_image[losepage_count]
        elif losepage_count == 4 and nextpage_button.draw(surf):
            break
        if losepage_count == 4 and restart_button.draw(surf):
            restart = True
            break




        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # pygame.quit() =>會導致不正常關閉遊戲

                waiting = False
        pygame.display.update()
    return restart

def win_page(surf, clock):
    restart = False
    waiting = True
    winpage_count = 0
    nextpage_button = Button(WIN_WIDTH - 70, WIN_HEIGHT - 535, nextpage_image)
    restart_button = Button(WIN_WIDTH -160, WIN_HEIGHT -535, restart_image)
    win_image = [pygame.image.load(f"images/ENDING/WIN ending_{i}.jpg") for i in range(3)]

    win_image1 = win_image[0]
    while waiting:
        clock.tick(FPS)  ## 1秒只能做60次迴圈
        surf.blit(win_image1, (0, 0))
        ##建立按鈕
        if winpage_count == 2:
            nextpage_button.image = exit_image
        if winpage_count <= 1 and nextpage_button.draw(surf):
            winpage_count += 1
            win_image1 = win_image[winpage_count]
        elif winpage_count == 2 and nextpage_button.draw(surf):
            break
        if winpage_count == 2 and restart_button.draw(surf):
            restart = True
            break


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # pygame.quit() =>會導致不正常關閉遊戲

                waiting = False
        pygame.display.update()
    return restart
