'''An all purpose button for for the game!'''
import pygame
from . import colors
from .root import Component


class Button(Component):
    '''An all purpose button for for the game!'''

    def __init__(self, text):
        super().__init__()
        self.text = text

    def draw(self):
        '''
        This method is called every frame! Not terrible efficient, 
        but i don't feel like making it more efficient right now.
        '''
        screen = pygame.display.get_surface()
        width, height = (200, 50)
        x = screen.get_width()//2 - width//2
        y = screen.get_height()//2 - height//2
        pygame.draw.rect(screen, colors.FOREGROUND, (x, y, width, height))

        font = pygame.font.SysFont(None, 24)
        text = font.render(self.text, True, colors.HEADER)
        screen.blit(text, (screen.get_width()//2 - text.get_width()//2, 40))
