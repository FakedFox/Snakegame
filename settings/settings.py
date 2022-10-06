import random

width = 800                    # ширина игрового окна
height = 800                   # высота игрового окна

game_speed = 80                # Скорость змеи
block = 20                     # размер сетки

grass_color = (0, 174, 0)      # цвет травы
snake_body = (255, 255, 0)     # цвет тела змеи
apple_color = (255, 0, 0)      # цвет яблока
grid = (200, 200, 200)         # цвет сетки игрового поля

running = True                 # состоние игры в процессе\ выход
fps = 30                       # ФПС

snake_posX = width / block * (block / 2)       # положение змеи по Х
snake_posY = height / block * (block / 2)      # положение змеи по У
apple_posX = random.randrange(20, width - block, block)  # положение яблока по Х
apple_posY = random.randrange(20, height - block, block) # положение яблока по У
