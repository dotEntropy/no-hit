from pygame.sprite import Sprite
from pygame.math import Vector2
import math
from src.global_vars import GlobalVars
from src.parents.bullet import Bullet
from src.entities.player import Player


class BloomPattern(Sprite, Bullet):
    def __init__(self, angle_rad: float) -> None:
        super().__init__()
        self._init_movement_variables(angle_rad)
        Bullet.__init__(self, "bloom-bullet-far")
    
    def _init_movement_variables(self, angle_rad) -> None:
        init_pos_x = GlobalVars.client_w // 2
        init_pos_y = GlobalVars.client_h // 2
        self.pos = Vector2(init_pos_x, init_pos_y)
        self.vel = Vector2()
        self.speed = 500
        self.radius = 0
        self.angle_rad = angle_rad

    def update(self, dt: float, player: Player) -> None:
        self._handle_despawn()
        self._update_vel(dt)
        self._update_pos(dt)
        self._detect_proximity(player)
    
    def _update_vel(self, dt: float) -> None:
        radius = self.radius
        angle_rad = self.angle_rad
        norm_x = math.cos(angle_rad) * radius
        norm_y = -math.sin(angle_rad) * radius
        self.vel = Vector2(norm_x, norm_y) * self.speed
        self.angle_rad += 0.5 * dt
        self.radius += 0.1 * dt
