import pygame
MOUSE_OUT = 1
MOUSE_IN = 2

MouseOutEvent = pygame.event.Event(pygame.USEREVENT, subtype=MOUSE_OUT)
MouseInEvent = pygame.event.Event(pygame.USEREVENT, subtype=MOUSE_IN)
