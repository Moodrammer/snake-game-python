from pygame.math import Vector2
import pygame
import random

class FRUIT:
    def __init__(self, cell_size, cell_number):
        """Initializes a fruit

        Args:
            cell_size (int): The size of the cell in the virtual grid assumed
            cell_number (int): Number of cells in the virtual grid assumed
        """
        self.x = random.randint(0, cell_number-1)
        self.y = random.randint(0, cell_number-1)
        self.cell_size = cell_size
        self.fruit_color = (255, 0, 50)
        self.pos = Vector2(self.x, self.y)
        
    def draw_fruit(self, display):
        """draws a fruit at a random cell on the virtual grid

        Args:
            display (pygame.display): screen on which to draw the fruit surface
        """
        fruit_rect = pygame.Rect(int(self.pos.x * self.cell_size), int(self.pos.y * self.cell_size), self.cell_size, self.cell_size)
        pygame.draw.rect(display, self.fruit_color, fruit_rect)
        
