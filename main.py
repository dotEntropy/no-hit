import pygame 
import time

from config import *
from level import Level
from assets.assets import get_image


class Game:
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_mode([client_w, client_h], pygame.NOFRAME)
        pygame.display.set_caption("No Hit")
        pygame.display.set_icon(get_image("icon.png"))
        self.level = Level()
        self.clock = pygame.time.Clock()
    
    def run(self) -> None:
        pre_time = time.time() 
        while True:
            self.clock.tick(FPS)
            dt = time.time() - pre_time
            pre_time = time.time()
            self.level.run(dt)
            pygame.display.update()


if __name__ == "__main__":
    game = Game()
    game.run()
