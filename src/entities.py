import pygame
import engine
from engine.entity import Entity
from engine.event import EventListener

class Unit(Entity, EventListener):
    
    def __init__(self, x, y):
        Entity.__init__(self, pygame.rect.Rect(x, y, 40, 40))
        EventListener.__init__(self)
        self.set_draw_method(self.draw)
        
    def draw(self, screen):
        pygame.draw.rect(screen, (200, 0, 0), self.rect)
        
    def on_key_down(self, event):
        if event.unicode == 'w':
            self.on_event(engine.event.TICK, self.__move_up)
        elif event.unicode == 's':
            self.on_event(engine.event.TICK, self.__move_down)
        elif event.unicode == 'd':
            self.on_event(engine.event.TICK, self.__move_right)
        elif event.unicode =='a':
            self.on_event(engine.event.TICK, self.__move_left)
    
    def on_key_up(self, event):
        if event.unicode == 'w':
            self.remove_event_function(engine.event.TICK, self.__move_up)
        elif event.unicode == 's':
            self.remove_event_function(engine.event.TICK, self.__move_down)
        elif event.unicode == 'd':
            self.remove_event_function(engine.event.TICK, self.__move_right)
        elif event.unicode =='a':
            self.remove_event_function(engine.event.TICK, self.__move_left)
            
    def __move_up(self, event):
        self.rect.y -= 10
    def __move_down(self, event):
        self.rect.y += 10
    def __move_left(self, event):
        self.rect.x -= 10
    def __move_right(self, event):
        self.rect.x += 10