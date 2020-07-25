import random
import pygame

# constant for window
WINDOW_RECT = pygame.Rect(0, 0, 480, 700)
# constant for refresh frame
FRAME_PER_SEC = 60
# constant for enemy timer event
ENEMY_TIMER = pygame.USEREVENT
# constant for bullet timer event
BULLET_TIMER = pygame.USEREVENT + 1


class GameSprite(pygame.sprite.Sprite):
    """Aircraft Game Sprite"""

    def __init__(self, img_name, speed=2):
        super().__init__()
        self.image = pygame.image.load(img_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        self.rect.y += self.speed


class Background(GameSprite):
    """Background class"""

    def __init__(self, is_alt=False):
        super().__init__("./images/background.png")
        if is_alt:
            self.rect.y = - self.rect.height

    def update(self):
        super().update()
        # 1. justify if the img out of window
        if self.rect.y >= WINDOW_RECT.height:
            self.rect.y = - self.rect.height


class Enemy(GameSprite):
    """Enemy class"""

    def __init__(self):
        super().__init__("./images/enemy1.png")
        self.speed = random.randint(2, 4)
        self.rect.bottom = 0
        max_x = WINDOW_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)

    def update(self):
        super().update()
        if self.rect.y >= WINDOW_RECT.height:
            self.kill()


class Hero(GameSprite):
    """Hero class"""

    def __init__(self):
        super().__init__("./images/me1.png", 0)
        self.rect.centerx = WINDOW_RECT.centerx
        self.rect.bottom = WINDOW_RECT.bottom - 120

        self.bullets = pygame.sprite.Group()

    def update(self):
        self.rect.x += self.speed
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > WINDOW_RECT.right:
            self.rect.right = WINDOW_RECT.right

    def fire(self):
        for i in (0, 1, 2):
            # 1. Make a bullet sprites
            bullet = Bullet()
            # 2. Set the position
            bullet.rect.bottom = self.rect.y - i * 20
            bullet.rect.centerx = self.rect.centerx
            # 3. add it to group
            self.bullets.add(bullet)


class Bullet(GameSprite):
    """Bullet class"""

    def __init__(self):
        super().__init__("./images/bullet1.png", -2)

    def update(self):
        super().update()
        if self.rect.bottom < 0:
            self.kill()
