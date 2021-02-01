'''
contains getter and setter for the root component, which
is drawn by the main game loop
'''

import pygame
from . import events

_root_component = None


def get():
    '''
    Gets the root component, which is currently being drawn
    each frame. @return None if the main component hasn't
    been set yet.
    '''
    global _root_component
    return _root_component


def assign_to(component):
    global _root_component
    _root_component = component


class Component:
    '''The base component class for all components in the game.'''

    def __init__(self, rect: pygame.Rect):
        self._subcomponents = []
        self.event_callbacks = {}
        self.draw_function = lambda: None
        self.rect = rect
        self.last_event = None

    def add_subcomponent(self, component):
        '''
        Add a subcomponent component to this component. When this
        component's update and draw function is called, it
        will call its subcomponents as well.
        '''
        self._subcomponents.append(component)

    def remove_subcomponent(self, component):
        '''removes the component from this components subcomponent list'''
        self._subcomponents.remove(component)

    def recursive_update(self, event):
        '''
        calls all the callback functions stored in this component
        for the given event, and also calls the update method for
        all subcomponents of this component
        '''
        x, y = pygame.mouse.get_pos()
        if self.event_callbacks.get(event.type) and self.rect.collidepoint(x, y):
            for function in self.event_callbacks[event.type]:
                function(event)
                
        if self.rect.collidepoint(x, y):
            self.last_event = event
        
        if self.last_event and self.last_event.type == pygame.MOUSEMOTION and not self.rect.collidepoint(x, y):
            pygame.event.post(events.MouseOutEvent)
            self.last_event = None
                
        for subcomponent in self._subcomponents:
            subcomponent.recursive_update(event)

    def recursive_draw(self):
        '''
        Calls this component's draw_function, which can be set with
        component.on_draw(your_function).
        
        Calls the recursive_draw method for all subcomponents of this component.
        '''
        self.draw_function(pygame.display.get_surface())
        for subcomponent in self._subcomponents:
            subcomponent.recursive_draw()
            
    def on_event(self, event_type, callback):
        '''registers a function to be called whenever this component recieves an certain event type'''
        if not self.event_callbacks.get(event_type):
            self.event_callbacks[event_type] = []
            
        self.event_callbacks[event_type].append(callback)
        
    def on_draw(self, draw_function):
        '''
        Sets the draw function for this component.
        '''
        self.draw_function = draw_function
