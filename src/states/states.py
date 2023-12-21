import pygame
from pygame.event import Event
import sys
from src.global_vars import GlobalVars
from src.states.game import GameState


class States:
    def __init__(self) -> None:
        self.game = GameState()
        GlobalVars.active_state = self.game
    
    def run(self, dt: float) -> None:
        self.active_state = GlobalVars.active_state
        self.active_state.update(dt)
        self.active_state.draw()
        self._handle_events()

    def _handle_events(self) -> None:
        for event in pygame.event.get():
            self._quit_event(event)
            self._key_down_events(event)
            self._mouse_events(event)

        keys = pygame.key.get_pressed()
        self.active_state.handle_key_held(keys)

        mouse_buttons = pygame.mouse.get_pressed()
        self.active_state.handle_mouse_held(mouse_buttons)
    
    def _key_down_events(self, event: Event) -> None:
        if event.type != pygame.KEYDOWN: return
        self.active_state.handle_key_tap(event.key)
    
    def _mouse_events(self, event: Event) -> None:
        if event.type != pygame.MOUSEBUTTONDOWN: return
        self.active_state.handle_mouse_tap(event.button)
        

    @staticmethod
    def _quit_event(event: Event) -> None:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type != pygame.KEYDOWN:
            return
        if event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()
