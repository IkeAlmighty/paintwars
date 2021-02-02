import pygame
import engine
from engine.event import EventManager
from engine.ui import Button

engine.init([500, 500])
event_manager = EventManager()
        
exit_button = Button("Exit To Desktop", (100, 100))
exit_button.on_click(lambda e: pygame.event.post(pygame.event.Event(pygame.QUIT)))

event_manager.add_listener(exit_button, pygame.MOUSEMOTION)

engine.draw_queue().add_entity(exit_button)
engine.start_game(event_manager)
