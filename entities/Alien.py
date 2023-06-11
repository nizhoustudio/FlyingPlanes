import random

import pygame


class Alien:
    def __init__(self, path):
        self.img = pygame.image.load(path)
        self.x = random.randint(100, 700)
        self.y = random.randint(10, 100)
        self.step = random.randint(1, 2)

    def show(self, screen):
        screen.blit(self.img, (self.x, self.y))

    def move(self):
        self.x += self.step
        if self.x > 736 or self.x < 0:
            self.step *= -1
            self.y += random.randint(1, 4)

    def reset(self):
        self.x = random.randint(100, 700)
        self.y = random.randint(10, 100)
        self.step = random.randint(1, 2)

    def over(self):
        if self.y >= 400:
            return True
        else:
            return False


def create_aliens(__max: int):
    __aliens = []
    for i in range(__max):
        __aliens.append(Alien("./assets/images/alien1.png"))
    return __aliens


def show_aliens(__aliens, __screen):
    for alien in __aliens:
        alien.show(__screen)


def move_aliens(__aliens):
    for alien in __aliens:
        alien.move()



