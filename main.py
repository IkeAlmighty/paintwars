import pygame
import engine
from engine.event import EventManager
from engine.ui import Button, Label

engine.init([500, 500])
event_manager = EventManager()
        
exit_button = Button("Exit To Desktop", (100, 100))
exit_button.on_click(lambda e: pygame.event.post(pygame.event.Event(pygame.QUIT)))
event_manager.add_listener(exit_button, pygame.MOUSEMOTION)

width, height = pygame.display.get_surface().get_size()
header = Label("Paint Wars", (100, 50, 50), (width//2, 10))

engine.draw_queue.add_entity(
    exit_button,
    header
    )
engine.cursor.set_image('pointer.png')
engine.start_game(event_manager) # should always be called last, as it loops until exit
