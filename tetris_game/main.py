# Game Structure 
# Definitions --------------------------------------------------
import pygame, sys

pygame.init()

    # Defining the variables needed
DARK_BLUE = (44, 44, 127)

screen = pygame.display.set_mode((300, 600))
pygame.display.set_caption('Python Tetris')

clock = pygame.time.Clock()
    # Creating the game objects 

# Game Loop --------------------------------------------------
    # 1. Event Handling 
    # 2. Updating Positions 
    
while True:
    for event in pygame.event.get():
        print(event.type)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # 3. Drawing Objects
    screen.fill(DARK_BLUE)
    pygame.display.update()
    clock.tick(60) # numbers of frames per second 
    # Updating the positions of the game objects 
    # Checking for collisions
