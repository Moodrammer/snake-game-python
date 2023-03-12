import pygame
from pygame.math import Vector2
from constants import DIRECTIONS


class SNAKE:
    def __init__(self, cell_size, cell_number):
        self.cell_size = cell_size
        self.cell_number = cell_number
        self.snake_color = pygame.Color('blue')
        self.direction = DIRECTIONS['RIGHT']
        self.body_cells = [Vector2(5,10), Vector2(6, 10), Vector2(7, 10)]
        self.is_add_new_block = False
        
    def draw_snake(self, display):
        head_rect = pygame.Rect(int(self.get_head_pos().x * self.cell_size), int(self.get_head_pos().y * self.cell_size), self.cell_size, self.cell_size)
        pygame.draw.rect(display, pygame.Color('black'), head_rect)
        
        for i in range(1, len(self.body_cells)):
            body_cell = self.body_cells[i]
            body_cell_rect = pygame.Rect(int(body_cell.x * self.cell_size), int(body_cell.y * self.cell_size), self.cell_size, self.cell_size)
            pygame.draw.rect(display, self.snake_color, body_cell_rect)
            
    def _is_reverse_direction(self, dir1, dir2):
        if (dir1 == DIRECTIONS['LEFT'] and dir2 == DIRECTIONS['RIGHT']) or (dir1 == DIRECTIONS['RIGHT'] and dir2 == DIRECTIONS['LEFT']):
            return True
        if (dir1 == DIRECTIONS['UP'] and dir2 == DIRECTIONS['DOWN']) or (dir1 == DIRECTIONS['DOWN'] and dir2 == DIRECTIONS['UP']):
            return True
        return False
    
    def set_snake_direction(self, direction: Vector2):
        if not self._is_reverse_direction(self.direction, direction):
            self.direction = direction
        
    def move_snake(self):
        head_cell = [self.body_cells[0] + self.direction]
        # check for boundaries
        if head_cell[0].x >= self.cell_number:
            head_cell[0].x = 0
        if head_cell[0].x < 0:
            head_cell[0].x = self.cell_number-1
        if head_cell[0].y >= self.cell_number:
            head_cell[0].y = 0
        if head_cell[0].y < 0:
            head_cell[0].y = self.cell_number-1
        
        if self.is_add_new_block:
            self.body_cells = head_cell + self.body_cells[:]
            self.is_add_new_block = False
        else:
            self.body_cells = head_cell + self.body_cells[:-1]
        
    def get_head_pos(self):
        return self.body_cells[0]
    
    def set_new_block_flag(self):
        self.is_add_new_block = True