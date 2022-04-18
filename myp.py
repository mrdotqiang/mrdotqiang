import pygame
from  plane_sprites import *



pygame.init()

screen = pygame.display.set_mode((480,700))

#backgroud image
bg = pygame.image.load("./images/background.png")
screen.blit(bg,(0,0))
#pygame.display.update()  统一调用一次即可

#warplane image
plane = pygame.image.load("./images/me1.png")
screen.blit(plane,(200,500))

pygame.display.update()

#时钟对象
clock = pygame.time.Clock()
plane_rect = pygame.Rect(200,500,102,126)

#创建敌机的精灵
enemy = GameSprite('./images/enemy1.png')
enemy1 = GameSprite('./images/enemy1.png',2)
#创建敌机的精灵组
enemy_group = pygame.sprite.Group(enemy,enemy1)

while True:
    clock.tick(60)

    #event_list = pygame.event.get()
    #if len(event_list) > 0:

    for event in pygame.event.get():
         if event.type == pygame.QUIT:
            print('quit the game!')
            pygame.quit()
            exit()
    #飞机移动的位置
    plane_rect.y -= 1
    #判断飞机的位置
    if plane_rect.y <= 0:
        plane_rect.y = 700

    screen.blit(bg,(0,0))
    screen.blit(plane,plane_rect)
    #精灵组的2个函数
    enemy_group.update()
    enemy_group.draw(screen)

    pygame.display.update()




pygame.quit()