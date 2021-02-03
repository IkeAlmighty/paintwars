'''
Contains common User Interface Classes. 
'''

import os
import pygame
from .event import EventListener
from .entity import ComponentEntity

class Button(EventListener, ComponentEntity):
    '''
    Basic Button Class for creating simple text buttons
    '''
    
    def __init__(self, text, pos):
        super().__init__()
        self.text = text
        
        # used to track click events
        self.click_down = False 
        self.on_click_functions = []
        
        # create the text image:
        font_dir = os.path.abspath('assets/fonts/Blockheads.ttf')
        self.image = pygame.font.Font(font_dir, 34).render(self.text, True, (255, 255, 255))
        
        text_w, text_h = self.image.get_rect().size
        self.rect = pygame.Rect(pos[0], pos[1], text_w + 10, text_h + 10)
        self.color = (100, 100, 100)
        
        self.set_draw_method(self._draw)
        
    def _draw(self, screen):
        '''default draw method'''
        pygame.draw.rect(screen, self.color, self.rect)
        x, y = self.rect.topleft
        screen.blit(self.image, (x + 5, y + 5))
    
    def on_mouse_motion(self, event):
        x, y = event.pos
        
        if self.rect.collidepoint(x, y):
            self.color = (0, 0, 200)
        else: 
            self.color = (100, 100, 100)
            
    def on_mouse_button_down(self, event):
        x, y = event.pos
        if self.rect.collidepoint(x, y):
            self.click_down = True
            
            self.color = (200, 100, 100)
            
    def on_mouse_button_up(self, event):
        x, y = event.pos
        if self.rect.collidepoint(x, y):
            # call all on_click functions:
            if self.click_down:
                for function in self.on_click_functions:
                    function(event)
            
            # inverse the color for click animation:
            self.color = (0, 0, 200)
                
        self.click_down = False
            
    def on_click(self, function):
        '''
        Add a function to be called when this component
        is clicked. The button must be added to an event
        manager via manager.add_listener(button_name)
        for this function to work.
        '''
        
        self.on_click_functions.append(function)
        
        
class Label(ComponentEntity, EventListener):
    
    def __init__(self, text, color, pos):
        super().__init__()
        self.text = text
        
        # create the text image:
        font_dir = os.path.abspath('assets/fonts/Blockheads.ttf')
        self.image = pygame.font.Font(font_dir, 72).render(self.text, True, color)
        x, y = pos
        x = x - self.image.get_width()//2
        self.rect = pygame.Rect(x, y, self.image.get_width(), self.image.get_height())
        self.color = (100, 100, 100)
        
        self.set_draw_method(self._draw)
        
    def _draw(self, screen):
        '''default draw method'''
        screen.blit(self.image, self.rect.topleft)