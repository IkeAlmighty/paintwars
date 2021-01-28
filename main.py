import pygame
from events.eventlogic import process_event
from entities.data import get_all_entities
from entities.graphics import draw_frame

pygame.init()

screen = pygame.display.set_mode([500, 500])

RUNNING = True
while RUNNING:
    for event in pygame.event.get():
        process_event(event)

    for entity in get_all_entities():
        draw_frame(entity)
