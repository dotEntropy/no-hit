import pygame
from pygame.sprite import Group, GroupSingle, collide_mask
from pygame.math import Vector2
import math
import numpy as np
import random

from config import *
from global_vars import Globals
from utils.clock import Timer

from entities.player import Player
from entities.spiral_bullet import SpiralBullet


class Level:
    def __init__(self) -> None:
        self._init_config()
        self._init_sprite_groups()
        self._init_sprite_instances()
        self._init_stage_sequence()
    
    # INITIALIZATION

    def _init_config(self) -> None:
        self.WIN = pygame.display.get_surface()
        self.spiral_shift = 0

    def _init_sprite_groups(self) -> None:
        self.player_group = GroupSingle() 
        self.bullet_group = Group()

    def _init_sprite_instances(self) -> None:
        self.player = Player()
        self.player.add(self.player_group)
    
    def _init_stage_sequence(self) -> None:
        self.spiral_stage = Timer(200, self._create_spiral)
        self.stage_index = -1
        self.stages = {
            "spiral_stage_0": {
                "type": self.spiral_stage,
                "time": 60_000
                },
            "spiral_stage_1": {
                "type": self.spiral_stage,
                "time": 15000
                }
        }

        self.current_stage = None
        self.stage_timer = Timer(0, self._update_stage)
        self.stage_timer.start()

    # LOOP

    def run(self, dt: float) -> None:
        self._handle_events()
        self._handle_updates(dt)
        self._draw_to_window()

    # EVENTS

    def _handle_events(self) -> None:
        keys = pygame.key.get_pressed()
        self.player.update_forces(keys)
        for event in pygame.event.get():
            self._quit_event(event)
            if event.type != pygame.KEYDOWN: continue
            self._handle_keydown_events(event.key)
    
    def _handle_keydown_events(self, key: int) -> None:
        if key == pygame.K_f:
            self._create_spiral()
        if key == pygame.K_SPACE:
            self._empty_spiral()
        if key == pygame.K_1:
            self.stage_timer.toggle_pause()
            self._toggle_pause_current_stage()
    
    def _create_spiral(self) -> None:
        for i in np.arange(0, 1, 0.1):
            angle_rad = math.tau*i + self.spiral_shift
            spiral_bullet = SpiralBullet(angle_rad)
            spiral_bullet.add(self.bullet_group)
        random_shift = random.random() * 0.25
        self.spiral_shift = (self.spiral_shift - random_shift) % math.tau
    
    def _empty_spiral(self) -> None:
        self.bullet_group.empty()

    @staticmethod
    def _quit_event(event: pygame.event.Event) -> None:
        if event.type == pygame.QUIT:
            Globals.running = False
        if event.type != pygame.KEYDOWN:
            return
        if event.key == pygame.K_ESCAPE:
            Globals.running = False
    
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
        
    # UPDATES

    def _handle_updates(self, dt: float) -> None:
        self._update_groups(dt)
        self._update_timers()
        # if pygame.sprite.spritecollide(self.player, self.bullet_group, False, collide_mask):
        #     self._empty_spiral()
    
    def _update_groups(self, dt: float) -> None:
        self.player_group.update(dt)
        self.bullet_group.update(dt)
    
    def _update_timers(self) -> None:
        self.spiral_stage.update()
        self.stage_timer.update()

    # DRAW

    def _draw_to_window(self) -> None:
        self.WIN.fill(Globals.bg_color)
        self.player_group.draw(self.WIN)
        self.bullet_group.draw(self.WIN)
    
