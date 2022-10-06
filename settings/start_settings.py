import pygame
from settings.settings import *

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

def gameset():                                   # окно игры

    pygame.init()
    pygame.display.set_caption("Snake")
    clock.tick(fps)
    screen.fill(grass_color)           # отрисовка окна
    pygame.display.flip()           # отрисовка окна буферизация


def drawGrid ():            #сетка на поле

    for x in range(0, width, block):
        for y in range(20, height, block):
            rect = pygame.Rect(x, y, block, block)
            pygame.draw.rect(screen, grid, rect, 1)

def screenset(running):

    pygame.event.set_blocked([pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP, pygame.MOUSEWHEEL, pygame.MOUSEMOTION])
    pygame.mouse.set_visible(False)  # отключает отображение мыши в игре
    pygame.event.set_grab(True)  # не дает мышке выйти за предела поля игры

    pygame.display.update()
    screen.fill(grass_color)
    if running == 'quit':
        return False
    else:
        return True

def eventCLK():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return 'quit'
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return 'quit'
            if event.key == pygame.K_LEFT:  # движение влево
                return 'left'
            elif event.key == pygame.K_RIGHT:  # двжение вправо
                return 'right'
            elif event.key == pygame.K_UP:  # движение вверх
                return 'up'
            elif event.key == pygame.K_DOWN:  # движение вниз
                return 'down'


