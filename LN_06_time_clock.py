import pygame

pygame.init()

surface = pygame.display.set_mode((480, 700))

# 1. create background
background = pygame.image.load("./images/background.png")
surface.blit(background, (0, 0))

# 3. create hero
hero = pygame.image.load("./images/me1.png")
surface.blit(hero, (200, 500))

# 3. update window
pygame.display.update()

# 4. create clock object
clock = pygame.time.Clock()

while True:
    clock.tick(60)  # 60/s

pygame.quit()
