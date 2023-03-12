import pygame
from pygame.math import Vector2


class SNAKE:
    def __init__(self, cell_size):
        self.cell_size = cell_size
        self.snake_color = pygame.Color('blue')
        self.body_cells = [Vector2(5,10), Vector2(6, 10), Vector2(7, 10)]
        
    def draw_snake(self, display):
        for body_cell in self.body_cells:
            body_cell_rect = pygame.Rect(body_cell.x * self.cell_size, body_cell.y * self.cell_size, self.cell_size, self.cell_size)
            pygame.draw.rect(display, self.snake_color, body_cell_rect)