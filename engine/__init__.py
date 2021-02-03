'''module for starting the game'''

import os
import pygame
from .event import EventListener
from .entity import Entity

class _Cursor (Entity):    
    
    def __init__(self):
        super().__init__()
        self.image = None
        self.set_draw_method(self._draw)
    
    def set_image(self, filename):
        if filename is None: 
            pygame.mouse.set_visible(True)
            self.image = None
        else:
            filepath = os.path.abspath('assets/images/cursors/{}'.format(filename))
            pygame.mouse.set_visible(False)
            self.image = pygame.image.load(filepath)
            self.image = pygame.transform.scale(self.image, (25, 25))
        
    def _draw(self, screen):
        if self.image or not pygame.mouse.get_visible():
            screen.blit(self.image, pygame.mouse.get_pos())
        
cursor = _Cursor()

class _DrawQueue:
    
    def __init__(self):
        self._queue = []
    
    def add_entity(self, *args):
        for entity in args:
            self._queue.append(entity)
        
    def draw_all(self):
        for entity in self._queue:
            entity.do_draw_method()
            
draw_queue = _DrawQueue()

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
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return
            
            event_manager.notify(event)
            draw_queue.draw_all()
            

        # keeps the framerate from going to high (but not too low, low depends on our code)
        clock.tick(60)
        
        # displays all the graphical updates that have been made.
        pygame.display.flip()
