import pygame
from src.global_vars import GlobalVars


class State:
    def __init__(self, state_alias: str) -> None:
        self.WIN = pygame.display.get_surface()
        try:
            GlobalVars.states[state_alias] = self
        except AttributeError:
            print("Specify a concise and valid state alias.")

    def change_state(self, new_state_alias: str) -> None:
        state = GlobalVars.states.get(new_state_alias)
        if state is None:
            print(f"State [{new_state_alias}] not found. Perhaps you mispelled the state alias?")
            return
        GlobalVars.active_state = state 
