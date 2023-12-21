import pygame
from pygame.sprite import Group, GroupSingle, Sprite
from pygame.event import Event
from pygame.math import Vector2
import math
import numpy as np
import random
from src.parents.state import State
from src.global_vars import GlobalVars
from src.assets import assets
from src.utils.clock import Timer
from src.entities.player import Player
from src.entities.bloom import SpiralBullet


class GameState(State):
    def __init__(self) -> None:
        super().__init__("game")
        self._init_config()
        self._init_groups()
        self._init_sprites()
        self._init_stage_sequence()
    
    # INITIALIZATION

    def _init_config(self) -> None:
        self.spiral_shift = 0

    def _init_groups(self) -> None:
        self.player_group = GroupSingle()
        self.bullet_group = Group()

    def _init_sprites(self) -> None:
        self.player = Player()
        self.player_group.add(self.player)
    
    def _init_stage_sequence(self) -> None:
        self.bloom = Timer(175, self._create_bloom)
        self.stage_index = -1
        self.stages = {
        "bloom_stage_0": {
            "type": self.bloom,
            "time": 30_000
            },
        }
        self.current_stage = None
        self.stage_timer = Timer(0, self._update_stage)
        self.stage_timer.start()
            
    # UPDATES

    def update(self, dt: float) -> None:
        self.dt = dt
        self.mouse_pos = Vector2(pygame.mouse.get_pos())
        self._update_groups()
        self._update_timers()


    def _update_groups(self) -> None:
        self.bullet_group.update(self.dt)
        self.player_group.update(self.dt)

    def _update_timers(self) -> None:
        self.bloom.update()
        self.stage_timer.update()

    # DRAW

    def draw(self) -> None:
        self.WIN.fill(GlobalVars.bg_color)
        self.bullet_group.draw(self.WIN)
        self.player_group.draw(self.WIN)

    # EVENTS
    
    def handle_key_tap(self, key: int):
        if key == pygame.K_f:
            self._create_bloom()
        if key == pygame.K_SPACE:
            self.bullet_group.empty()
        if key == pygame.K_1:
            self.stage_timer.toggle_pause()
            self._toggle_pause_current_stage()
    
    def handle_mouse_tap(self, button: int):
        pass

    def handle_key_held(self, keys: dict) -> None:
        self.player.update_forces(keys)

    def handle_mouse_held(self, buttons: tuple) -> None:
        pass

    # BULLET FUNCTIONS

    def _create_bloom(self) -> None:
        for i in np.arange(0, 1, 0.1):
            angle_rad = math.tau*i + self.spiral_shift
            spiral_bullet = SpiralBullet(angle_rad)
            spiral_bullet.add(self.bullet_group)
        random_shift = random.random() * 0.5
        self.spiral_shift = (self.spiral_shift - random_shift) % math.tau

    # STAGE FUNCTIONS

    def _update_stage(self) -> None:
        self.stage_index += 1
        # no more stages?
        if self.stage_index > len(self.stages) - 1:
            self.stage_timer.stop()
            self._stop_current_stage()
            return
        self._stop_current_stage()
        self._start_new_stage()
        self._start_current_stage()
    
    def _stop_current_stage(self) -> None:
        if self.current_stage is None: return
        self.current_stage.stop()

    def _start_new_stage(self) -> None:
        stages = self.stages
        stage_id = list(stages.keys())[self.stage_index]
        stage = stages[stage_id]
        self.current_stage: Timer = stage["type"]
        self.current_stage_time = stage["time"]
        self.stage_timer.change_interval(self.current_stage_time)

    def _start_current_stage(self) -> None:
        if self.current_stage is None: return
        self.current_stage.start()
    
    def _toggle_pause_current_stage(self) -> None:
        if self.current_stage is None: return
        self.current_stage.toggle_pause()
    
