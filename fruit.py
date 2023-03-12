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
        self.cell_number = cell_number
        self.cell_size = cell_size
        self.fruit_color = (255, 0, 50)
        self.fruit_asset = pygame.image.load('Graphics/tomato.png')
        self.set_new_fruit_pos()
        
    def draw_fruit(self, display):
        """draws a fruit at a random cell on the virtual grid

        Args:
            display (pygame.display): screen on which to draw the fruit surface
        """
        fruit_rect = pygame.Rect(int(self.pos.x * self.cell_size), int(self.pos.y * self.cell_size), self.cell_size, self.cell_size)
        # pygame.draw.rect(display, self.fruit_color, fruit_rect)
        display.blit(self.fruit_asset, fruit_rect)
        
    def set_new_fruit_pos(self):
        self.x = random.randint(0, self.cell_number-1)
        self.y = random.randint(0, self.cell_number-1)
        self.pos = Vector2(self.x, self.y)  
        
