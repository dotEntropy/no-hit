import pygame
import time
from src.states.states import States
from src.global_vars import GlobalVars
from src.assets import assets
from src.utils.debug_text import DebugText


class Main:
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption("no-hit")
        pygame.display.set_icon(assets.get_image("icon.png"))
        display_info = pygame.display.Info()
        GlobalVars.client_w = display_info.current_w
        GlobalVars.client_h = display_info.current_h
        self.clock = pygame.time.Clock()
        self.states = States()
        self.debug = DebugText()

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
            f"fps: {round(self.clock.get_fps())}"
            ], rate_ms=50)
        self.debug.draw()


if __name__ == "__main__":
    try:
        game = Main()
        game.run()
    except KeyboardInterrupt:
        pygame.quit()
