'''contains getter and setter for the root component, which is drawn by the main game loop'''

import pygame

_root_component = None


def get():
    '''Gets the root component, which is currently being drawn each frame. @return None if the main component hasn't been set yet.'''
    global _root_component
    return _root_component


def assign_to(component):
    global _root_component
    _root_component = component


class Component:
    '''The base component class for all components in the game.'''

    def __init__(self):
        self._children = []
        self.event_callbacks = {}

    def add_child(self, component):
        '''Add a child component to this component. When this component's update and draw function is called, it will call it's children's as well.'''
        self._children.append(component)

    def remove_child(self, component):
        '''removes the component from this components child list'''
        self._children.remove(component)

    def update(self, event):
        '''calls all the callback functions stored in this component for the given event, and also calls the update method for all children of this component'''
        for child in self._children:
            child.update(event)
        
        if self.event_callbacks.get(event.type):
            for function in self.event_callbacks[event.type]:
                function(event)

    def draw(self):
        '''Calls the draw method for all children of this component'''
        for child in self._children:
            child.draw()
            
    def on_event(self, event_type, callback):
        '''registers a function to be called whenever this component recieves an certain event type'''
        if not self.event_callbacks.get(event_type):
            self.event_callbacks[event_type] = []
            
        self.event_callbacks[event_type].append(callback)
