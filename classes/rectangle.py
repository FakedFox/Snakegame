from settings.start_settings import *

class Rectangle():
    def __init__(self,screen, block, startXpos, startYpos, color):
        self.block = block
        self.startXpos = startXpos
        self.startYpos = startYpos
        self.color = color
        self.screen = screen
    def start(self):
        self.rect = pygame.Rect(self.startXpos, self.startYpos, self.block, self.block)
        pygame.draw.rect(self.screen, self.color, self.rect)

    def position(self):
        return [self.startXpos, self.startYpos]

