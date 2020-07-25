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

