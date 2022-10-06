from classes.rectangle import Rectangle
from settings.start_settings import width, height
import random

class Apple(Rectangle):

    def __init__(self, screen, block, startXpos, startYpos, color):
        super().__init__(screen, block, startXpos, startYpos, color)

    def rePosApple(self):
        self.startXpos = random.randrange(self.block, width - self.block, self.block)
        self.startYpos = random.randrange(self.block, height - self.block, self.block)
