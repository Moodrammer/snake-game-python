import pygame as pg
import sys

pg.init()
gameWidth, gameHeight = 400, 500
screen = pg.display.set_mode((gameWidth, gameHeight)) # creating a display surface
screen.fill((175, 215, 70))

test_surface = pg.Surface((100, 200))
test_surface.fill(pg.Color('blue'))
test_rectangle = test_surface.get_rect(center=(200, 250))

clock = pg.time.Clock()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    
    screen.blit(test_surface, test_rectangle) # blit : block image transfer
    
    
    pg.display.update()
    clock.tick(60) # Running at 60 fps as a maximum rate
