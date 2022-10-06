from settings.start_settings import *
from classes.rectangle import Rectangle


class Snake(Rectangle):
    direction = ''
    oldDir = ''

    def __init__(self, screen, block, startXpos, startYpos, color, game_speed):
        super().__init__(screen, block, startXpos, startYpos, color)
        self.game_speed = game_speed
        self.snakeLen = [[startXpos, startYpos]]

    def start(self):
        Rectangle.start(self)
        for i in self.snakeLen:
            rect = pygame.Rect(i[0], i[1], self.block, self.block)
            pygame.draw.rect(screen, self.color, rect)

    def move(self, direct):
        if direct != None:
            self.direction = direct

        if (self.direction == 'left') and self.oldDir != 'right':  # движение влево
            self.oldDir = 'left'
            self.startXpos -= self.block
            self.rect = (self.startXpos, self.startYpos, self.startXpos, self.startYpos)
            self.snakeLen.append([self.startXpos, self.startYpos])
            self.snakeLen.pop(0)
        elif (self.direction == 'right') and self.oldDir != 'left':  # двжение вправо
            self.oldDir = 'right'
            self.startXpos += self.block
            self.rect = (self.startXpos, self.startYpos, self.startXpos, self.startYpos)
            self.snakeLen.append([self.startXpos, self.startYpos])
            self.snakeLen.pop(0)

        elif (self.direction == 'up') and self.oldDir != 'down':  # движение вверх
            self.oldDir = 'up'
            self.startYpos -= self.block
            self.rect = (self.startXpos, self.startYpos, self.startXpos, self.startYpos)
            self.snakeLen.append([self.startXpos, self.startYpos])
            self.snakeLen.pop(0)

        elif (self.direction == 'down') and self.oldDir != 'up':  # движение вниз
            self.oldDir = 'down'
            self.startYpos += self.block
            self.rect = (self.startXpos, self.startYpos, self.startXpos, self.startYpos)
            self.snakeLen.append([self.startXpos, self.startYpos])
            self.snakeLen.pop(0)
        else:
            self.direction = self.oldDir

        pygame.time.wait(self.game_speed)


    def snake_len(self):
        return self.snakeLen

    def grow(self):
        self.snakeLen.append(self.position())

