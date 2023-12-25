import pygame
from pygame.sprite import Group, GroupSingle
from pygame.math import Vector2
import math
import numpy as np
import random
from src.parents.state import State
from src.global_vars import GlobalVars
from src.utils.clock import Timer
from src.entities.player import Player
from src.entities.bloom import BloomPattern


class GameState(State):
    def __init__(self) -> None:
        super().__init__("game")
        self._init_config()
        self._init_groups()
        self._init_sprites()
        self._init_attack_types()
        self._init_stage_sequence()
    
    # INITIALIZATION

    def _init_config(self) -> None:
        GlobalVars.game_over = False
        self.spiral_shift = 0

    def _init_groups(self) -> None:
        self.player_group = GroupSingle()
        self.bullet_group = Group()

    def _init_sprites(self) -> None:
        self.player = Player()
        self.player_group.add(self.player)
    
    def _init_attack_types(self) -> None:
        self.attack_types = {
            "bloom": Timer(175, self._create_bloom_attack)
        }
    
    def _init_stage_sequence(self) -> None:
        self.stage_index = 0
        self.stages = {
            "bloom-stage-0": {
                "type": self.attack_types["bloom"],
                "duration": 30_000
                },
            }
        self.current_attack = None
        self.stage_timer = Timer(0, self._update_stage)
        self.stage_timer.start()
            
    # UPDATES

    def update(self, dt: float) -> None:
        self.dt = dt
        self.mouse_pos = Vector2(pygame.mouse.get_pos())
        self._update_groups()
        self._check_game_over()
        self._update_current_attack()
        self.stage_timer.update()

    def _update_groups(self) -> None:
        self.bullet_group.update(self.dt, self.player)
        self.player_group.update(self.dt)
    
    def _check_game_over(self) -> None:
        if GlobalVars.game_over:
            self.__init__()
            GlobalVars.attempts += 1

    # DRAW

    def draw(self) -> None:
        self.WIN.fill(GlobalVars.bg_color)
        self.bullet_group.draw(self.WIN)
        self.player_group.draw(self.WIN)

    # EVENTS
    
    def handle_key_tap(self, key: int):
        pass
    
    def handle_mouse_tap(self, button: int):
        pass

    def handle_key_held(self, keys: dict) -> None:
        self.player.handle_controls(keys)

    def handle_mouse_held(self, buttons: tuple) -> None:
        pass

    # ATTACKS

    def _create_bloom_attack(self) -> None:
        for i in np.arange(0, 1, 0.1):
            angle_rad = math.tau*i + self.spiral_shift
            spiral_bullet = BloomPattern(angle_rad)
            spiral_bullet.add(self.bullet_group)
        random_shift = random.random() * 0.5
        self.spiral_shift = (self.spiral_shift - random_shift) % math.tau

    # STAGES

    def _update_stage(self) -> None:
        # no more stages?
        if self.stage_index > len(self.stages) - 1:
            self.stage_timer.stop()
            self._stop_current_attack()
            return
        self._stop_current_attack()
        self._start_new_stage()
        self._start_current_attack()
    
    def _start_new_stage(self) -> None:
        stages = self.stages
        self.current_stage_id = list(stages.keys())[self.stage_index]
        self.current_stage = stages[self.current_stage_id]
        self.current_attack: Timer = self.current_stage["type"]
        self.current_stage_duration: int = self.current_stage["duration"]
        self.stage_timer.change_interval(self.current_stage_duration)
        self.stage_index += 1
    
    def _update_current_attack(self) -> None:
        if self.current_attack is None: return
        self.current_attack.update()

    def _start_current_attack(self) -> None:
        if self.current_attack is None: return
        self.current_attack.start()

    def _stop_current_attack(self) -> None:
        if self.current_attack is None: return
        self.current_attack.stop()
    
    def _toggle_pause_current_attack(self) -> None:
        if self.current_attack is None: return
        self.current_attack.toggle_pause()
