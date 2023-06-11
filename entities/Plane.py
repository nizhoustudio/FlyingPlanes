import pygame


class Plane:
    def __init__(self, path: str, x: int, y: int, step: int):
        self.img = pygame.image.load(path)
        self.x = x
        self.y = y
        self.step = step

    def move(self, left, right):
        self.x += self.step
        if self.x > right:
            self.x = right
        if self.x < left:
            self.x = left


if __name__ == "__main__":
    plane = Plane("1", 2, 2016, 1)
    print(plane.x, plane.y, plane.step)
