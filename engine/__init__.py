'''module for starting the game'''

import pygame

_draw_queue = None

def draw_queue():
    global _draw_queue
    if _draw_queue == None:
        _draw_queue = _DrawQueue()
        
    return _draw_queue

class _DrawQueue:
    
    def __init__(self):
        self._queue = []
    
    def add_entity(self, entity):
        self._queue.append(entity)
        
    def draw_all(self):
        for entity in self._queue:
            entity.do_draw_method()

def init(resolution, fullscreen=False):
    pygame.init()
    
    if fullscreen:
        pygame.display.set_mode(resolution, flags=pygame.FULLSCREEN)
    else:
        pygame.display.set_mode(resolution)

def start_game(event_manager):
    
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return
            
            event_manager.notify(event)
            draw_queue().draw_all()
            

        # keeps the framerate from going to high (but not too low, low depends on our code)
        clock.tick(60)
        
        # displays all the graphical updates that have been made.
        pygame.display.flip()
