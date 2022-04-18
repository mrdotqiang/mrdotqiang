import pygame
from  plane_sprites import *


class PlaneGame(object):
    """飞机大战主游戏"""
    def __init__(self):
        print('游戏初始化')
        #set window
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        #set clock
        self.clock = pygame.time.Clock()
        #invoke private func to create sprite and sprite_group
        self.__create_sprites()

        # 设置定时器事件 - 创建敌机  1s
        pygame.time.set_timer(CREATE_ENEMY_EVENT,1000)
        pygame.time.set_timer(PLANE_FIRE_EVENT,500)


    def __create_sprites(self):
        bg1 = BackGround()
        bg2 = BackGround(True)
        #bg2.rect.y = -bg2.rect.height
        self.back_group = pygame.sprite.Group(bg1,bg2)

        self.enemy_group = pygame.sprite.Group()

        self.plane = Plane()
        self.plane_group = pygame.sprite.Group(self.plane)


    def start_game(self):
        print('游戏开始..')

        while True:
            #set clock
            self.clock.tick(FRAME_PER_SEC)
            #set event
            self.__event_handler()
            #check collide
            self.__check_collide()
            #update sprites
            self.__update_sprites()
            #update display
            pygame.display.update()

    # set event
    def __event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
               # print('敌机出场...')
                enmey = Enemy()
                self.enemy_group.add(enmey)
            elif event.type == PLANE_FIRE_EVENT:
                self.plane.fire()
            #elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            #    print('向右移动')
        #使用键盘提供的方法获取键盘按键 - 按键元组
        keys_pressed = pygame.key.get_pressed()
        # 判断元组中的对应的按键索引值 1
        if keys_pressed[pygame.K_RIGHT]:
            #print('向右移动...')
            self.plane.speed = 12
        elif keys_pressed[pygame.K_LEFT]:
            self.plane.speed = -12
        else:
            self.plane.speed = 0

    def __check_collide(self):
        #子弹摧毁敌机
        pygame.sprite.groupcollide(self.plane.bullet_group,self.enemy_group,True,True)
        #敌机撞飞机
        enemies_list = pygame.sprite.spritecollide(self.plane,self.enemy_group,True)
        #
        if len(enemies_list) > 0:
            self.plane.kill()
            PlaneGame.__game_over()

    def __update_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.plane_group.update()
        self.plane_group.draw(self.screen)

        self.plane.bullet_group.update()
        self.plane.bullet_group.draw(self.screen)


    @staticmethod
    def __game_over():
        print('game over!!!')
        pygame.quit()
        exit()

if __name__ == '__main__':
    game = PlaneGame()
    game.start_game()
