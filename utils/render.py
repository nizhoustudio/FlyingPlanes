import pygame


def render(text, color, screen, location):
    font = pygame.font.Font('freesansbold.ttf', 32)
    text_render = font.render(text, True, color)
    screen.blit(text_render, location)
