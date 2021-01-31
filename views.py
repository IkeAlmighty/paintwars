'''Contains all the different root views to be used in the game.'''

import pygame
from engine.components.button import Button
from engine.components.root import Component
from engine.components import colors

class TitleScreen(Component):
    
    def __init__(self):
        super().__init__(pygame.display.get_surface().get_rect())
        exit_button = Button('Exit to Desktop', 100, 100)
        exit_button.on_event(pygame.MOUSEBUTTONUP, self.close)
        self.add_subcomponent(exit_button)
        self.on_draw(self.draw)
    
    def draw(self, screen):
        screen = pygame.display.get_surface()
        font = pygame.font.SysFont(None, 24)
        img = font.render('PAINT WARS', True, colors.HEADER)
        screen.blit(img, (screen.get_width()//2 - img.get_width()//2, 40))
    
    def close(self, event):
        pygame.event.post(pygame.event.Event(pygame.QUIT))
        