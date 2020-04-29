import pygame

# ============================== OUTDATED ORIGINAL GAME HUD CONCEPT ===============================================

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
black = (0, 0, 0)
halfw = int(SCREEN_WIDTH /2)


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def title_display(text, screen):
    largeText = pygame.font.Font('freesansbold.ttf', 30)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (halfw , 40)
    screen.blit(TextSurf, TextRect)


def points_display(text, screen):
    largeText = pygame.font.Font('freesansbold.ttf', 20)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (halfw - 120, 80)
    screen.blit(TextSurf, TextRect)


def health_display(text, screen):
    largeText = pygame.font.Font('freesansbold.ttf', 20)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (halfw , 80)
    screen.blit(TextSurf, TextRect)


def lives_display(text, screen):
    largeText = pygame.font.Font('freesansbold.ttf', 20)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (halfw + 120, 80)
    screen.blit(TextSurf, TextRect)


def text_update(sc, health, lives, screen):
    points_display(('Score: ' + str(sc)), screen)
    health_display(('Health: ' + str(health)), screen)
    lives_display(('Lives: ' + str(lives)), screen)
    title_display(('Level 1: Escape Guantanamo Bay'), screen)