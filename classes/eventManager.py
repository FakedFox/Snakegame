from settings.start_settings import *

class EventManager():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def score(self,snakeLen):
        font = pygame.font.SysFont(None, 24)
        img = font.render(f'Score - "{len(snakeLen) -1}"', True, grid)
        screen.blit(img, (10, 3))

    def eat(self, snake_pos, apple_pos):
        if snake_pos == apple_pos:
            return True

    def limitation(self, snake_pos):
        if snake_pos[0] not in range(self.width) or snake_pos[1] not in range(10, self.height):
            return True

    def suicide(self, snakeLen):
        for i in snakeLen[0 : -2]:
            if snakeLen[-1] == i:
                return True

    def endGame(self, snakeLen):
        font = pygame.font.SysFont(None, int(width / 5))
        img = font.render(f'Score - "{len(snakeLen) - 1}"', True, grid)
        screen.blit(img, (self.width / 20, self.height / 3))

        #return False

