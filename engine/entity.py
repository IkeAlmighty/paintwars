from abc import ABC
import pygame

class Entity(ABC):
    
    def __init__(self):
        self._draw_method = lambda: None
        
    def set_draw_method(self, method):
        self._draw_method = method
        
    def do_draw_method(self):
        self._draw_method(pygame.display.get_surface())
    

class ComponentEntity(Entity, ABC): pass