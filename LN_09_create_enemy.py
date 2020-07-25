from GM_plane_sprites import *  # 4.3

pygame.init()

surface = pygame.display.set_mode((480, 700))

# 1. create background
background = pygame.image.load("./images/background.png")
surface.blit(background, (0, 0))

# 3. create hero
hero = pygame.image.load("./images/me1.png")
surface.blit(hero, (185, 500))

# 3. update window
pygame.display.update()

# 4. create clock object
clock = pygame.time.Clock()

# 5. use rect to remember the position of hero
hero_rect = pygame.Rect(185, 500, 102, 126)

# Create enemy
enemy = GameSprite("./images/enemy1.png")
enemy1 = GameSprite("./images/enemy1.png", 2)
# Create enemy group
enemy_group = pygame.sprite.Group(enemy,enemy1)

while True:
    clock.tick(60)  # 60/s
    # 10. get event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    # 6. change position of hero
    hero_rect.y -= 1
    # 9. if y <=0, change that back to buttom
    if hero_rect.y <= -126:
        hero_rect.y = 700
    # 7. use blit method
    surface.blit(background, (0, 0))
    surface.blit(hero, hero_rect)

    # enemy group call update
    enemy_group.update()
    # enemy group call draw
    enemy_group.draw(surface)

    # 8. use update method
    pygame.display.update()

pygame.quit()
