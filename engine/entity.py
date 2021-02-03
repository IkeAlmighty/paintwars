from abc import ABC
import os
import pygame


class Entity(ABC):

    def __init__(self, rect: pygame.rect.Rect):
        self._draw_method = lambda: None
        self.rect = rect
        self.last_draw_rect = None

    def set_draw_method(self, method):
        self._draw_method = method

    def do_draw_method(self):
        screen = pygame.display.get_surface()
        self._draw_method(screen)
        self.last_draw_rect = self.rect.copy()


class ComponentEntity(Entity, ABC):
    pass

class EntityDrawManager:
    
    def __init__(self):
        self._collision_map = {} # maps an entity to entities that collide with it
        self._queue = [] # holds a queue of entities that need to be redrawn
    
    def _register_entity_collisions(self, new_entity):
        # find all entities that collied with this new entity,
        # and also add this new enitity to their collision lists.
        new_entity_collisions = []
        for entity in self._collision_map.keys():
            if entity.rect.colliderect(new_entity.rect):
                new_entity_collisions.append(entity)
                self._collision_map[entity].append(new_entity)
                
        self._collision_map[new_entity] = new_entity_collisions
    
    def add_entity(self, *args):
        for entity in args:
            if not self._collision_map.get(entity):
                self._register_entity_collisions(entity)
                
            self._queue.append(entity)
        
    def draw_all(self):
        redraw_queue = []
        for entity in self._queue:
            # erase (if it's been drawn once),
            if entity.last_draw_rect:
                pygame.draw.rect(pygame.display.get_surface(), (0, 0, 0), entity.last_draw_rect)
            
            # add collisions to redraw queue:
            collision_update_queue = []
            for collision in self._collision_map[entity]:
                redraw_queue.append(collision)
                # flag update for collision map:
                if not entity.rect.colliderect(collision.rect):
                    collision_update_queue.append(collision)
            
            # update the collision map:
            for collision in collision_update_queue:
                self._collision_map[entity].remove(collision)
                self._collision_map[collision].remove(entity)
            
            # add this entity to the end of the redraw queue:
            redraw_queue.append(entity)
            
        # redraw everything added to the redraw queue
        # (this will include all of the initial _queue entities + their collisions):
        # print('redraw queue:', redraw_queue)
        for entity in redraw_queue:
            entity.do_draw_method()
            
class Cursor (Entity):
    
    def __init__(self):
        Entity.__init__(self, pygame.rect.Rect(0, 0, 0, 0))
        self.image = None
        self.set_draw_method(self._draw)
    
    def set_image(self, filename):
        if filename is None: 
            pygame.mouse.set_visible(True)
            self.image = None
        else:
            filepath = os.path.abspath('assets/images/cursors/{}'.format(filename))
            pygame.mouse.set_visible(False)
            self.image = pygame.image.load(filepath)
            self.image = pygame.transform.scale(self.image, (25, 25))
            self.rect = self.image.get_rect()
            print(self.rect)
        
    def _draw(self, screen):
        if self.image:
            self.rect.topleft = pygame.mouse.get_pos()
            screen.blit(self.image, self.rect.topleft)