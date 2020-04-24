import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
black = (0, 0, 0)
halfw = int(SCREEN_WIDTH /2)


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def points_display(text, screen):
    largeText = pygame.font.Font('freesansbold.ttf', 20)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (halfw - 120, 50)
    screen.blit(TextSurf, TextRect)


def title_display(text, screen):
    largeText = pygame.font.Font('freesansbold.ttf', 30)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (halfw , 20)
    screen.blit(TextSurf, TextRect)


def health_display(text, screen):
    largeText = pygame.font.Font('freesansbold.ttf', 20)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (halfw , 50)
    screen.blit(TextSurf, TextRect)


def lives_display(text, screen):
    largeText = pygame.font.Font('freesansbold.ttf', 20)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (halfw + 120, 50)
    screen.blit(TextSurf, TextRect)


def text_update(sc, health, lives, screen):
    points_display(('Score: ' + str(sc)), screen)
    health_display(('Health: ' + str(health)), screen)
    lives_display(('Lives: ' + str(lives)), screen)
    title_display(('Level 1: Escape Guantanamo Bay'), screen)