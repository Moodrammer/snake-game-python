import pygame
from pygame.math import Vector2
from fruit import FRUIT
from snake import SNAKE
from constants import DIRECTIONS
import sys

pygame.init()


# Game Global Variables
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_size * cell_number, cell_size * cell_number)) # creating a display surface
clock = pygame.time.Clock()

# Game User-defined events
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

# Main game class
class GAME:
    def __init__(self):
        self.fruit = FRUIT(cell_size, cell_number)
        self.snake = SNAKE(cell_size, cell_number)
        
    def update(self):
        self.snake.move_snake()
   
    def draw_elements(self):
        self.fruit.draw_fruit(screen)
        self.snake.draw_snake(screen)    

game = GAME()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            game.update()  
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                game.snake.set_snake_direction(DIRECTIONS['UP'])
            if event.key == pygame.K_DOWN:
                game.snake.set_snake_direction(DIRECTIONS['DOWN'])
            if event.key == pygame.K_LEFT:
                game.snake.set_snake_direction(DIRECTIONS['LEFT'])
            if event.key == pygame.K_RIGHT:
                game.snake.set_snake_direction(DIRECTIONS['RIGHT'])
        
    
    screen.fill((175, 215, 70))
    game.draw_elements()
    
    pygame.display.update()
    clock.tick(60) # Running at 60 fps as a maximum rate
