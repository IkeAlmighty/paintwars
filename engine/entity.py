from abc import ABC
import pygame


class Entity(ABC):

    def __init__(self, rect: pygame.rect.Rect):
        self._draw_method = lambda: None
        self.rect = rect

    def set_draw_method(self, method):
        self._draw_method = method

    def do_draw_method(self):
        screen = pygame.display.get_surface()
        
        # then, draw again:
        self._draw_method(screen)


class ComponentEntity(Entity, ABC):
    pass
