import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
black = (0, 0, 0)


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def message_display(text, screen):
    largeText = pygame.font.Font('freesansbold.ttf', 20)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (SCREEN_WIDTH - 60, 30)
    screen.blit(TextSurf, TextRect)


def points_update(sc, screen):
    message_display(('Score: ' + str(sc)), screen)
