'''module for starting the game'''

import pygame
from . import components

def start(resolution, root_component_class, fullscreen=False):
    pygame.init()
    
    if fullscreen:
       pygame.display.set_mode(resolution, flags=pygame.FULLSCREEN)
    else:
        pygame.display.set_mode(resolution)
    
    root_component = root_component_class()
    components.root.assign_to(root_component)
    
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return
            
            components.root.get().recursive_update(event) # will update all child components of the root component
            components.root.get().recursive_draw() # will draw this component and all its children
            

        # keeps the framerate from going to high (but not too low, low depends on our code)
        clock.tick(60)
        
        # displays all the graphical updates that have been made.
        pygame.display.flip()
