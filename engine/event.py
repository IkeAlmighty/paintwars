'''
Provides Concrete EventManager class and Abstract 
EventListener class for controlling game pygame events.
'''

import re
import pygame

def camel_to_snake(name: str):
    '''takes the name and converts it to snake case'''
    name = re.sub(R'(?<!^)(?=[A-Z])', '_', name).lower()
    return name

class EventManager():
    '''
    Provides a concrete class for objects to register themselves as listeners
    to, so that they can easily execute code on pygame events. This class would
    be considered the 'Subject' in the Observer design pattern.
    '''
    
    def __init__(self):
        self.listeners = {}
    
    def notify(self, event):
        '''
        Calls corresponding snake case style on_<event_name> methods
        of all EventListener objects that have registered to this
        Event Manager.
        '''
        for event_type in self.listeners.values():
            for listener in event_type:
                listener.do_event(event)
        
    def add_listener(self, listener, event_type):
        if not self.listeners.get(event_type):
            self.listeners[event_type] = []
            
        self.listeners[event_type].append(listener)
        

class EventListener:
    
    def do_event(self, event):
        '''
        Calls the corresponding on_<event_snake_case>(event)
        method in this listener, if such a method has been
        implemented.
        '''
        event_name_snake_case = camel_to_snake(pygame.event.event_name(event.type))
        for member in dir(self):
            if member == "on_{}".format(event_name_snake_case):
                attr = getattr(self, member)
                attr(event)
            
            