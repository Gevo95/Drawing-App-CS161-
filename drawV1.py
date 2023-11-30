# added erase feature but it currently requires both left and right click simultaneously see lines 35 and on 
import pygame
import sys

pygame.init()

# sets the dimensions for the painting window this can be changed just made it small 
WIDTH, HEIGHT = 750, 300
BG_COLOR = (0, 0, 0) # 0 0 0 is a black background white would be 255 255 255 (look up RGB python colors) 
DRAW_COLOR = (255, 255, 0) # yellow not sure how to do multi color options
LINE_WIDTH = 3   
ERASER_WIDTH = 4 

# this sections creates the pygame window 
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("VERSION ONE PAINTER ")

drawing = False # mouse held down will equal painting/ True   
last_pos = None # stores the last mouse position. 
erase = False

clock = pygame.time.Clock() # there seem to be some input lag wonder if its the same for you adjusting FPS is a way to limit how much CPU game uses 
FPS = 30

### We need a while loop for the main loop of the game to handle the various actions/ events. 
while True:
   clock.tick(FPS) # part of FPS capping . 
   
   for event in pygame.event.get(): 
    if event.type == pygame.QUIT: ## this is so user can quit the game 
        pygame.quit()
        sys.exit
      
    if event.type == pygame.MOUSEBUTTONDOWN: #maps left click as drawing when pressed down. 
       if event.button == 1:
          drawing = True
          last_pos = event.pos

       if event.button == 3: # 34-35 map R click as eraser 3 is python "mapping" for lack of better term for R click but for some reason requiring L & R click error is somewhere around here xD 
          erase = True  
    
    if event.type == pygame.MOUSEMOTION:
       if drawing:
          current_pos = event.pos
          if not erase:
            pygame.draw.line(screen, DRAW_COLOR , last_pos, current_pos,LINE_WIDTH)
          else:
             pygame.draw.line(screen,BG_COLOR,last_pos,current_pos,ERASER_WIDTH) 
          last_pos = current_pos
 

    if event.type == pygame.MOUSEBUTTONUP: 
       if event.button == 1:
        drawing = False # drawing = False makes it so that when we release L mouse it no longer tracks movement as drawing 

       if event.button == 3:
         erase = False 
        
   
   pygame.display.flip() # updates display 
