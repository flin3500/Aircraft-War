import pygame
from GM_plane_sprites import *


class AircraftGame(object):
    """Aircraft main"""

    def __init__(self):
        # 1. create window
        self.window = pygame.display.set_mode(WINDOW_RECT.size)
        # 2. create clock
        self.clock = pygame.time.Clock()
        # 3. Create sprites and sprites Group
        self.__create_sprites()

        pygame.time.set_timer(ENEMY_TIMER, 1000)
        pygame.time.set_timer(BULLET_TIMER, 500)

    def __create_sprites(self):
        bg1 = Background()
        bg2 = Background(is_alt=True)
        self.back_group = pygame.sprite.Group(bg1, bg2)
        self.enemy_group = pygame.sprite.Group()
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    def start_game(self):
        while True:
            # 1.set refresh rate
            self.clock.tick(FRAME_PER_SEC)
            # 2.check user input
            self.__event_handler()
            # 3.check collision
            self.__check_collision()
            # 4.Update and draw sprites Group
            self.__update_sprites()
            # 5.Update the window
            pygame.display.update()

    def __event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                AircraftGame.__game_over()
            elif event.type == ENEMY_TIMER:
                enemy = Enemy()
                self.enemy_group.add(enemy)
            elif event.type == BULLET_TIMER:
                self.hero.fire()
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_RIGHT]:
            self.hero.speed = 3
        elif keys_pressed[pygame.K_LEFT]:
            self.hero.speed = -3
        else:
            self.hero.speed = 0

    def __check_collision(self):
        # 1. bullet kill enemy
        pygame.sprite.groupcollide(self.hero.bullets, self.enemy_group, True, True)
        # 2. Enemy kill hero
        collide = pygame.sprite.groupcollide(self.hero_group, self.enemy_group, True, True)
        if len(collide) > 0:
            AircraftGame.__game_over()

    def __update_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.window)
        self.enemy_group.update()
        self.enemy_group.draw(self.window)
        self.hero_group.update()
        self.hero_group.draw(self.window)
        self.hero.bullets.update()
        self.hero.bullets.draw(self.window)

    @staticmethod
    def __game_over():
        print("GAME OVER!")
        pygame.quit()
        exit()


if __name__ == '__main__':
    game = AircraftGame()
    game.start_game()
