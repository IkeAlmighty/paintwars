'''Contains all the different root views to be used in the game.'''

import pygame
from engine.components.button import Button
from engine.components.root import Component
from engine.components import colors

class TitleScreen(Component):
    
    def __init__(self, *args):
        super().__init__(pygame.display.get_surface().get_rect())
        
        for subcomponent in args:
            self.add_subcomponent(subcomponent)
            
        self.on_draw(self.draw)
    
    def draw(self, screen):
        screen = pygame.display.get_surface()
        font = pygame.font.SysFont(None, 24)
        img = font.render('PAINT WARS', True, colors.HEADER)
        screen.blit(img, (screen.get_width()//2 - img.get_width()//2, 40))
        