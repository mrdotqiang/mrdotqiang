import random
import pygame

#游戏窗口大小设置
SCREEN_RECT = pygame.Rect(0,0,480,700)
#刷新的帧率
FRAME_PER_SEC = 60
#敌机定时器常量
CREATE_ENEMY_EVENT = pygame.USEREVENT
#发射子弹事件
PLANE_FIRE_EVENT = pygame.USEREVENT + 1

class GameSprite(pygame.sprite.Sprite):

   def __init__(self,image_name,speed=1):

       super().__init__()

       self.image = pygame.image.load(image_name)
       self.rect = self.image.get_rect()
       self.speed = speed

   def update(self):
       self.rect.y += self.speed

class BackGround(GameSprite):

    def __init__(self,is_alt=False):
        super().__init__('./images/background.png')
        # 交替图像，需要设置初使位置
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):
        super().update()
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height

class Enemy(GameSprite):
    def __init__(self):
        super().__init__('./images/enemy1.png')

        self.speed = random.randint(1,3)

        self.rect.bottom = 0

        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0,max_x)

    def update(self):
        super().update()
        if self.rect.y >= SCREEN_RECT.height:
           # print('飞出屏幕，需要从精灵组删除...')
            self.kill()

    def __del__(self):
        #print('敌机挂了 %s' % self.rect)
        pass

class Plane(GameSprite):
    def __init__(self):
        super().__init__('./images/me1.png',0)
        #飞机位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120

        #创建子弹精灵组
        self.bullet_group = pygame.sprite.Group()

    # 飞机移动
    def update(self):
        self.rect.x += self.speed

        #判断是否移出屏幕
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

    def fire(self):
        print('发射子弹..')

        for i in (0,1,2):
            #设置子弹精灵
            bullet = Bullet()
            #子弹位置
            bullet.rect.bottom = self.rect.y - i * 20
            bullet.rect.centerx = self.rect.centerx
            #将精妙添加到精灵组
            self.bullet_group.add(bullet)

class Bullet(GameSprite):
    def __init__(self):
        super().__init__('./images/bullet1.png',-3)


    def update(self):
        super().update()
        #判断子弹飞出屏幕
        if self.rect.bottom < 0:
            self.kill()

    def __del__(self):
        print('子弹销毁..')






