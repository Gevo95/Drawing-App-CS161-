import pygame
import sys

pygame.init()

# sets the dimensions for the painting window
WIDTH, HEIGHT = 500,300
BG_COLOR = (0, 0, 0) # 0 0 0 is a black background white would be 255 255 255 (look up RGB python colors) 
DRAW_COLOR = (255, 255, 255)
LINE_WIDTH = 3 

# this sections creates the pygame window 
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("VERSION ONE PAINTER ")

drawing = False # mouse held down will equal painting/ True   
last_pos = None # stores the last mouse position. 


### We need a while loop for the main loop of the game to handle the various actions/ events. 
while True: 
   for event in pygame.event.get(): ## this is so user can quit the game 
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit
 screen. fill (BG_COLOR) # TEST to see if code will generate screen
pygame.display.flip # updates display 
    
    
    
