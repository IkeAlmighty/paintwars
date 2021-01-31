'''An all purpose button for for the game!'''
import pygame
from . import colors
from .root import Component


class Button(Component):
    '''An all purpose button for for the game!'''

    def __init__(self, text, x, y):
        # the rect for Button is set to 0s initially, and then 
        # reassigned in this constructor, the new values based
        # on the text render size.
        super().__init__(pygame.Rect(0, 0, 0, 0)) 
        self.text = text
        
        font = pygame.font.SysFont(None, 24)
        self.text_img = font.render(self.text, True, colors.HEADER)
        
        text_width, text_height = self.text_img.get_size()
        self.rect = pygame.Rect(x, y, text_width + 10, text_height + 10)
        
        # setting the base draw function:
        self.on_draw(self.draw)
        
        # adding event handlers:
        self.on_event(pygame.MOUSEBUTTONDOWN, self.mouse_down)
        self.on_event(pygame.MOUSEBUTTONUP, self.mouse_up)

    def draw(self, screen):
        # draw the backgroud of the button:
        pygame.draw.rect(screen, colors.FOREGROUND, self.rect)

        # draw the button text:
        x, y = self.rect.topleft
        screen.blit(self.text_img, (x + 5, y + 5))
        
    def draw_mousedown(self, screen):
        # draw the background of the button:
        pygame.draw.rect(screen, colors.SELECTED, self.rect)

        # draw the button text:
        x, y = self.rect.topleft
        screen.blit(self.text_img, (x + 5, y + 5))
        
    def mouse_down(self, event):
        self.on_draw(self.draw_mousedown)
    
    def mouse_up(self, event):
        self.on_draw(self.draw)
