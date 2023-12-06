import pygame 
import time
import sys

from config import *
from global_vars import Globals
from assets.assets import get_image
from utils.debug_text import DebugText
from level import Level


class Game:
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_mode([Globals.client_w, Globals.client_h], pygame.NOFRAME)
        pygame.mouse.set_visible(False)
        pygame.display.set_caption("No Hit")
        pygame.display.set_icon(get_image("icon.png"))
        self.debug = DebugText()
        self.level = Level()
        self.clock = pygame.time.Clock()
        self.pre_time = time.time() 
    
    def run(self) -> None:
        while Globals.running:
            self.dt = time.time() - self.pre_time
            self.pre_time = time.time()

            self.level.run(self.dt)
            self._update_debug()

            pygame.display.update()
            self.clock.tick(Globals.fps)

        pygame.quit()
        sys.exit()
    
    def _update_debug(self) -> None:
        try:
            self.debug.update_texts([
                f"fps: {self.clock.get_fps():.0f}",
                self.level.stage_timer.is_active,
                self.level.current_stage.is_active
                ], rate_ms=50)
            self.debug.draw()
        except:
            pass


if __name__ == "__main__":
    game = Game()
    game.run()
