import pygame

# constant for window
WINDOW_RECT = pygame.Rect(0, 0, 480, 700)
# constant for refresh frame
FRAME_PER_SEC = 60


class GameSprite(pygame.sprite.Sprite):
    """Aircraft Game Sprite"""

    def __init__(self, img_name, speed=1):
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
            #
            self.rect.y = - self.rect.height

    def update(self):
        super().update()
        # 1. justify if the img out of window
        if self.rect.y >= WINDOW_RECT.height:
            self.rect.y = - self.rect.height

