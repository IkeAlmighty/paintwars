
import inspect

def get_do_event_name(event):
    pass

class EventManager():
    
    def __init__(self):
        pass
    
    def notify(self, event):
        for event_type in self.listeners:
            for listener in event_type:
                listener.do_event(event)
        
    def add_listener(self, event_type, listener):
        self.listeners[event_type].append(listener)
        

class EventListener:
    
    def __init__(self):
        pass
    
    def do_event(self, event):
        if get_do_event_name(event) in dir(self):
            