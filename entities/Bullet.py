import pygame


def show_bullets(__bullets, __screen):
    # 绘制子弹组
    for bullet in __bullets:
        __screen.blit(bullet.img, (bullet.x, bullet.y))


def move_bullets(__bullets):
    for bullet in __bullets:
        bullet.move()
        if bullet.y < 0:
            __bullets.remove(bullet)


class Bullet:
    def __init__(self, path, x, y, step):
        self.img = pygame.image.load(path)
        self.x = x
        self.y = y
        self.step = step

    def move(self):
        self.y -= self.step

