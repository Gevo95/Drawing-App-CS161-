import pygame
import sys

pygame.init()

# sets the dimensions for the painting window
WIDTH, HEIGHT = 500,300
BG_COLOR = (0, 0, 0) # 0 0 0 is a black background white would be 255 255 255 (look up RGB python colors) 
DRAW_COLOR = (5, 5, 5)
LINE_WIDTH = 3 


screen = pygame.display.set.mode((WIDTH, HEIGHT))
pygame.display.set_caption("VERSION ONE PAINTER ")

drawing = False 
last_pos = None
### We need a while loop for the main loop of the game to handle the various actions/ events. 
while True: 
    
