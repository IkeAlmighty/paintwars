'''module for starting the game'''

import pygame
from .event import EventListener
from .entity import Entity, EntityDrawManager, Cursor
        
cursor = Cursor()

draw_queue = EntityDrawManager()

def init(resolution, fullscreen=False):
    pygame.init()
    
    if fullscreen:
        pygame.display.set_mode(resolution, flags=pygame.FULLSCREEN)
    else:
        pygame.display.set_mode(resolution)

def start_game(event_manager):
    
    draw_queue.add_entity(cursor)
    
    clock = pygame.time.Clock()
    while True:
        
        # process events and draws:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return
            
            event_manager.notify(event)
            draw_queue.draw_all()
            

        # keeps the framerate from going to high (but not too low, low depends on our code)
        clock.tick(60)
        
        # displays all the graphical updates that have been made.
        pygame.display.flip()
