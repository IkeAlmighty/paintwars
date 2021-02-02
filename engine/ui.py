
from .event import EventListener
from .entity import ComponentEntity
import pygame

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
        self.image = pygame.font.SysFont(None, 34).render(self.text, True, (255, 255, 255))
        
        text_w, text_h = self.image.get_rect().size
        self.rect = pygame.Rect(pos[0], pos[1], text_w + 10, text_h + 10)
        self.color = (100, 100, 100)
        
        self.set_draw_method(self.draw)
        
    def draw(self, screen):
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
            
    def on_mouse_button_up(self, event):
        x, y = event.pos
        if self.rect.collidepoint(x, y):
            for function in self.on_click_functions:
                function(event)
            
    def on_click(self, function):
        '''
        Add a function to be called when this component
        is clicked. The button must be added to an event
        manager via manager.add_listener(button_name)
        for this function to work.
        '''
        self.on_click_functions.append(function)