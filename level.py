import pygame
import sys

from config import *
from utils.clock import Timer
from utils.debug_text import DebugText

from entities.player import Player


class Level:
    def __init__(self) -> None:
        self._initialize_config()
        self._create_sprite_instances()
        self._create_sprite_groups()
    
    # INITIALIZATION

    def _initialize_config(self) -> None:
        self.tick_count = 0
        self.total_frames = 0
        self.debug = DebugText()
        self.WIN = pygame.display.get_surface()
        self.BG_COLOR = (20, 20, 20)
        self.pre_val = 0

    def _create_sprite_instances(self) -> None:
        self.player = Player()

    def _create_sprite_groups(self) -> None:
        self.player_group = pygame.sprite.GroupSingle() 
        self.player_group.add(self.player)

    # LOOP

    def run(self, dt: float) -> None:
        self._handle_events()
        self._handle_updates(dt)
        self._draw_to_window()

    # EVENTS

    def _handle_events(self) -> None:
        keys = pygame.key.get_pressed()
        self.player.update_forces(keys)
        self.debug.texts = [self.player.vel]
        for event in pygame.event.get():
            self._quit_event(event)

    @staticmethod
    def _quit_event(event: pygame.event.Event) -> None:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type != pygame.KEYDOWN:
            return
        if event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()
        
    # UPDATES

    def _handle_updates(self, dt: float) -> None:
        self.player_group.update(dt)
        # self._update_fps()

    def _update_fps(self) -> None:
        try:
            self.total_frames += 1 / self.player.dt
            if not self.tick_count:
                self.debug.texts = self.total_frames / 100
                self.total_frames = 0
        except ZeroDivisionError:
            pass
        self.tick_count = (self.tick_count + 1) % 100

    # DRAW

    def _draw_to_window(self) -> None:
        self.WIN.fill(self.BG_COLOR)
        self.debug.draw()
        self.player_group.draw(self.WIN)
    
