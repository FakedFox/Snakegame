from settings.start_settings import *
from classes.snake import Snake
from classes.apple import Apple
from classes.eventManager import EventManager

gameset()

snake = Snake(screen, block, snake_posX, snake_posY, snake_body, game_speed)
apple = Apple(screen, block, apple_posX, apple_posY, apple_color)
event = EventManager(width, height)

while running:

    drawGrid()
    direct = eventCLK()
    running = screenset(direct)

    snake.start()
    apple.start()

    snake.move(direct)

    if event.limitation(snake.position()) == True or event.suicide(snake.snake_len()) == True:
        event.endGame(snake.snake_len())
        running = False

    if event.eat(snake.position(), apple.position()):
        apple.rePosApple()
        snake.grow()

    event.score(snake.snake_len())


running = True
while running:

    event.endGame(snake.snake_len())
    running = screenset(eventCLK())