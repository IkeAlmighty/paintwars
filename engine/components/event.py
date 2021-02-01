import pygame

def post(event):
    print('posting event of type ', type(event))
    if isinstance(event, type(pygame.event.Event)):
        pygame.event.post(event)
    elif isinstance(event, type(Event(""))):
        pygame.event.post(pygame.event.Event(pygame.USEREVENT, data=event))

class Event:
    
    def __init__(self, event_type, data: dict = None):
        super().__init__()
        self.type = event_type
        self.data = data
        
    def __str__(self):
        return self.type + self.data.__str__()
    
    def __eq__(self, other):
        return self.__str__() == other.__str__()
    
    def __hash__(self):
        return self.data.__str__().__hash__()
    
MouseOutEvent = Event('MOUSE OUT')
