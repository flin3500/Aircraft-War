import pygame

pygame.init()

surface = pygame.display.set_mode((480, 700))

# 1. import image
background = pygame.image.load("./images/background.png")
# 2. surface blit method
surface.blit(background, (0, 0))
# 3. update window
pygame.display.update()

while True:
    pass

pygame.quit()
