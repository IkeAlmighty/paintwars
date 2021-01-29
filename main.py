'''Main Entry Point for the Program'''

import pygame
import components
from components import views

pygame.init()

screen = pygame.display.set_mode([400, 400])

clock = pygame.time.Clock()

RUNNING = True

title_screen = views.TitleScreen()
components.root.assign_to(title_screen)

while RUNNING:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            RUNNING = False
        
        components.root.get().update(event) # will update all child components of the root component
        components.root.get().draw() # will draw this component and all its children
        

    # keeps the framerate from going to high (but not too low, low depends on our code)
    clock.tick(60)
    
    # displays all the graphical updates that have been made.
    pygame.display.flip()
