'''Contains all the different root views to be used in the game.'''

import pygame
from .button import Button
from .root import Component
from . import colors

class TitleScreen(Component):
    
    def __init__(self):
        super().__init__()
        exit_button = Button('Exit to Desktop')
        exit_button.on_event(pygame.MOUSEBUTTONUP, self.close)
        self.add_child(exit_button)
    
    def draw(self):
        screen = pygame.display.get_surface()
        font = pygame.font.SysFont(None, 24)
        img = font.render('PAINT WARS', True, colors.HEADER)
        screen.blit(img, (screen.get_width()//2 - img.get_width()//2, 40))
    
    def close(self, event):
        pygame.event.post(pygame.event.Event(pygame.QUIT))
        