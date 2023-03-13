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
    def __init__(self, display):
        self.fruit = FRUIT(cell_size, cell_number)
        self.snake = SNAKE(cell_size, cell_number)
        self.game_font = pygame.font.Font('Fonts/nice_sugar/Nice Sugar.ttf', 25)
        self.display = display
        
    def update(self):
        self.check_collision()
        self.snake.move_snake()
        self.check_gameover()
   
    def draw_elements(self):
        self.draw_grass()
        self.fruit.draw_fruit(screen)
        self.snake.draw_snake(screen)
        self.draw_score()
        
    def check_collision(self):
        if self.snake.get_head_pos() == self.fruit.pos:
            # eat the fruit i.e plant a new fruit at another place
            self.fruit.set_new_fruit_pos()
            # make the snake larger
            self.snake.set_new_block_flag()
            
    def check_gameover(self):
        if self.snake.get_head_pos() in self.snake.body_cells[1:]:
            pygame.quit()
            sys.exit()
            
    def draw_grass(self):
        grass_color = (167, 209, 61)
        for row in range(cell_number):
            if row % 2 != 0:
                for col in range(cell_number):
                    if col % 2 != 0:
                        grass_rect = pygame.Rect(int(col * cell_size), int(row * cell_size), cell_size, cell_size)
                        pygame.draw.rect(self.display, grass_color, grass_rect)
            else:
                for col in range(cell_number):
                    if col % 2 == 0:
                        grass_rect = pygame.Rect(int(col * cell_size), int(row * cell_size), cell_size, cell_size)
                        pygame.draw.rect(self.display, grass_color, grass_rect)
                        
    def draw_score(self):
        score_text = str(int(len(self.snake.body_cells) - 3) * 10)
        score_surface = self.game_font.render(score_text, True, (56, 74, 12))
        score_x = int(cell_size * cell_number - 60)
        score_y = int(cell_size * cell_number - 50)
        score_rect = score_surface.get_rect(center=(score_x, score_y))
        tomato_rect = self.fruit.fruit_asset.get_rect(midright=(score_rect.left, score_rect.centery))
        score_bg_rect = pygame.Rect(tomato_rect.left, tomato_rect.top - 3, tomato_rect.width + score_rect.width + 6, tomato_rect.height + 3)
        
        pygame.draw.rect(self.display, (200, 200, 200), score_bg_rect)
        self.display.blit(score_surface, score_rect)
        self.display.blit(self.fruit.fruit_asset, tomato_rect)
        pygame.draw.rect(self.display, pygame.Color('black'), score_bg_rect, 2)
        
        

game = GAME(screen)

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
