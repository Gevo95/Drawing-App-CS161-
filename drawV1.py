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
   for event in pygame.event.get(): 
    if event.type == pygame.QUIT: ## this is so user can quit the game 
        pygame.quit()
        sys.exit         
    if event.type == pygame.MOUSEBUTTONDOWN: #maps left click as drawing when pressed down. 
       if event.button == l:
          drawing = True
          last_pos = event.pos
    if event.type == pygame.MOUSEMOTION:
       if drawing:
          current_pos = event.pos
          pygame.draw.line(screen, BLACK , last_pos, current_pos 5)

    if event.type == pygame.MOUSEBUTTONUP:
       if event.button == l:
          drawing = False
  ## screen. fill (BG_COLOR) # TEST to see if code will generate screen
pygame.display.flip # updates display 
    
    
    
