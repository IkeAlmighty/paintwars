import pygame
import engine
from engine.ui import Button, Label
from engine.entity import EntityContainer

engine.init([1080, 1080], fullscreen=True)

exit_button = Button("Exit To Desktop", (100, 100))
exit_button.on_click(lambda e: pygame.event.post(
    pygame.event.Event(pygame.QUIT))
)

width, height = pygame.display.get_surface().get_size()
header = Label("Paint Wars", (100, 50, 50), (width//2, 10))

titleScreen = EntityContainer(
    exit_button,
    header
)

engine.draw_queue.add_entity(titleScreen)
engine.cursor.set_image('pointer.png')

# should always be called last, as it loops until exit
engine.start_game()
