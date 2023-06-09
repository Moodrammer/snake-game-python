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
        self.fruit_asset_frame_1 = pygame.image.load('Graphics/tomato_1.png')
        self.fruit_asset_frame_2 = pygame.image.load('Graphics/tomato_2.png')
        self.frame_num = 0
        
        self.set_new_fruit_pos()
        
    def draw_fruit(self, display):
        """draws a fruit at a random cell on the virtual grid

        Args:
            display (pygame.display): screen on which to draw the fruit surface
        """
        fruit_rect = pygame.Rect(int(self.pos.x * self.cell_size), int(self.pos.y * self.cell_size), self.cell_size, self.cell_size)
        # pygame.draw.rect(display, self.fruit_color, fruit_rect)
        if self.frame_num >= 0 and self.frame_num <= 20:
            display.blit(self.fruit_asset, fruit_rect)
        elif self.frame_num <= 30:
            display.blit(self.fruit_asset_frame_1, fruit_rect)
        elif self.frame_num <= 60:
            display.blit(self.fruit_asset_frame_2, fruit_rect)
        elif self.frame_num <= 70:
            display.blit(self.fruit_asset_frame_1, fruit_rect)
        else:
            display.blit(self.fruit_asset_frame_1, fruit_rect)
            self.frame_num = 0
            
        self.frame_num += 1
        
    def set_new_fruit_pos(self):
        self.x = random.randint(1, self.cell_number-2)
        self.y = random.randint(1, self.cell_number-2)
        self.pos = Vector2(self.x, self.y)  
        
