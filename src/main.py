import pygame
import engine
from engine.ui import Button, Label
from engine.entity import EntityContainer, Entity
from engine.event import EventListener

from entities import Unit

class Game:
    
    def __init__(self):
        engine.init([500, 500])
        
        engine.cursor.set_image('assets/images/cursors/pointer.png')
        
        self.game_lobby = self.__create_game_lobby()
        self.start_screen = self.__create_start_screen()
        
        self.open_start_screen()
        
    def __create_game_lobby(self):
        return EntityContainer()
    
    def __create_start_screen(self):
        exit_button = Button("Exit To Desktop", (100, 150))
        exit_button.on_click(lambda e: pygame.event.post(
            pygame.event.Event(pygame.QUIT))
        )

        play_button = Button("New Game Lobby", (100, 100))
        play_button.on_click(lambda e: self.open_game_lobby())

        width, height = pygame.display.get_surface().get_size()
        header = Label("Paint Wars", (100, 50, 50), (width//2, 10))
        return EntityContainer(
            exit_button,
            play_button,
            header
        )
        
    def open_game_lobby(self):
        engine.clear_entities()
        engine.add_entity(self.game_lobby)
        
    def open_start_screen(self):
        engine.clear_entities()
        engine.add_entity(self.start_screen)
        
    def open_game(self, game_id=None):
        pass


if __name__ == "__main__":
    Game()
    
    # should always be called last, as it loops until exit
    engine.start_game()
    