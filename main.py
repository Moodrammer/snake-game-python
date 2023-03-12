import pygame as pg
from fruit import FRUIT
from snake import SNAKE
import sys

pg.init()

# Game Global Variables
cell_size = 40
cell_number = 20
screen = pg.display.set_mode((cell_size * cell_number, cell_size * cell_number)) # creating a display surface
screen.fill((175, 215, 70))
clock = pg.time.Clock()
f = FRUIT(cell_size, cell_number)
s = SNAKE(cell_size)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    
    f.draw_fruit(screen)
    s.draw_snake(screen)
    
    pg.display.update()
    clock.tick(60) # Running at 60 fps as a maximum rate
