import pygame
import sys

pygame.init()

# sets the dimensions for the painting window
WIDTH, HEIGHT = 500,300
BG_COLOR = (1, 1, 1)
DRAW_COLOR = (5, 5, 5)
LINE_WIDTH = 3 


screen = pygame.display.set.mode((WIDTH, HEIGHT))
pygame.display.set_caption("VERSION ONE PAINTER ")

drawing = False 
last_pos = None
### We need a while loop for the main loop of the game to handle the various actions/ events. 
while True: 
    