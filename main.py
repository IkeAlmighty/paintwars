import pygame
import engine
from engine.event import EventListener
from engine.entity import ComponentEntity

engine.init([500, 500])

# exit_button = engine.ui.Button('EXIT!', 100, 100)

# engine.start_game(views.TitleScreen(
#     exit_button
# ))

from engine.event import EventManager

event_manager = EventManager()

class Button(EventListener, ComponentEntity):
    
    def __init__(self, rect):
        super().__init__()
        self.text = "MY BUTTON"
        self.set_draw_method(self.draw)
        self.rect = rect
        self.color = (100, 100, 100)
        
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
    
    def on_mouse_motion(self, event):
        x, y = event.pos
        
        if self.rect.collidepoint(x, y):
            self.color = (0, 0, 200)
        else: 
            self.color = (100, 100, 100)
        
b = Button(pygame.Rect(100, 100, 100, 50))
event_manager.add_listener(b, pygame.MOUSEMOTION)

engine.draw_queue().add_entity(b)
engine.start_game(event_manager)
