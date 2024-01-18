import pygame
import time
import os
from src.states.states import States
from src.global_vars import GlobalVars
from src.assets.assets import load_assets
from src.utils.debug_text import DebugText


class Main:
    def __init__(self) -> None:
        self._init_display()
        self._init_assets()
        self.clock = pygame.time.Clock()
        self.states = States()
        self.debug = DebugText()
        
    def _init_display(self) -> None:
        pygame.init()
        os.system("cls")
        pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption("no-hit")
        display_info = pygame.display.Info()
        GlobalVars.client_w = display_info.current_w
        GlobalVars.client_h = display_info.current_h
        GlobalVars._update_sprite_scale()
    
    def _init_assets(self) -> None:
        load_assets()
        pygame.display.set_icon(GlobalVars.get_asset("icon"))

    def run(self) -> None:
        pre_time = time.time()
        while True:
            dt = time.time() - pre_time
            pre_time = time.time()
            self.states.run(dt)
            self._run_debug()
            pygame.display.update()
            self.clock.tick(GlobalVars.fps)
    
    def _run_debug(self) -> None:
        self.debug.update([
            f"{GlobalVars.client_w}x{GlobalVars.client_h}",
            f"fps: {round(self.clock.get_fps())}",
            f"attempts: {GlobalVars.attempts}",
            ], rate_ms=25)
        self.debug.draw()


if __name__ == "__main__":
    try:
        game = Main()
        game.run()
    except KeyboardInterrupt or Exception as e:
        print(e)
        pygame.quit()
