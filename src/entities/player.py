import pygame
from pygame.sprite import Sprite
from pygame.math import Vector2
from src.parents.update_image import UpdateImage
from src.global_vars import GlobalVars
from src.assets import assets
from src.utils import vectors


class Player(Sprite, UpdateImage):
    def __init__(self) -> None:
        super().__init__()
        self._init_movement_variables()
        UpdateImage.__init__(self, assets.get_image("player.png"))
    
    def _init_movement_variables(self) -> None:
        self.pos = Vector2(200, GlobalVars.client_h // 2)
        self.vel = Vector2()
        self.max_vel = 500
        self.accel = Vector2()
        self.force = Vector2()
        self.mass = Vector2(1, 1)
        self.force_applied = 5000
        self.friction = 2000
        self.bounce_power = 500
    
    def update(self, dt: float) -> None:
        self.dt = dt
        self._update_accel()
        self._update_vel()
        self._update_pos()
        self._update_accel()
    
    def update_forces(self, keys: dict) -> None:
        self.force = Vector2()
        if keys[pygame.K_a]:
            self.force.x -= self.force_applied
        if keys[pygame.K_d]:
            self.force.x += self.force_applied
        if keys[pygame.K_s]:
            self.force.y += self.force_applied
        if keys[pygame.K_w]:
            self.force.y -= self.force_applied
        if self.force: self.force.clamp_magnitude_ip(self.force_applied)
    
    def _update_accel(self) -> None:
        accel_x = self.force.x / self.mass.x
        accel_y = self.force.y / self.mass.y
        self.accel = Vector2(accel_x, accel_y)
    
    def _update_vel(self) -> None:
        self.dt_accel = self.accel * self.dt
        self._create_friction()
        self.vel += self.dt_accel
        if self.vel: self.vel.clamp_magnitude_ip(self.max_vel)
    
    def _create_friction(self) -> None:
        if not self.vel: return
        dt_friction = self.friction * self.dt
        if self.vel.x > 0:
            self.vel.x = max(self.vel.x - dt_friction, 0)
        if self.vel.x < 0:
            self.vel.x = min(self.vel.x + dt_friction, 0)
        if self.vel.y > 0:
            self.vel.y = max(self.vel.y - dt_friction, 0)
        if self.vel.y < 0:
            self.vel.y = min(self.vel.y + dt_friction, 0)

    def _update_pos(self) -> None:
        self.dt_vel = self.vel * self.dt
        self._check_border_collide()
        self.pos += self.dt_vel
        self.rect.centerx = round(self.pos.x)
        self.rect.centery = round(self.pos.y)

    def _check_border_collide(self) -> None:
        width_border = GlobalVars.client_w
        height_border = GlobalVars.client_h

        pos_next_frame_left = self.rect.left + self.dt_vel.x
        pos_next_frame_right = self.rect.right + self.dt_vel.x
        pos_next_frame_top = self.rect.top + self.dt_vel.y
        pos_next_frame_bottom = self.rect.bottom + self.dt_vel.y

        if pos_next_frame_left < 0:
            self.pos.x = self.rect.w // 2
            self.vel.x = self.bounce_power
        if pos_next_frame_right > width_border:
            self.pos.x = width_border - self.rect.w // 2
            self.vel.x = -self.bounce_power
        if pos_next_frame_top < 0:
            self.pos.y = self.rect.h // 2
            self.vel.y = self.bounce_power
        if pos_next_frame_bottom > height_border:
            self.pos.y = height_border - self.rect.h // 2
            self.vel.y = -self.bounce_power
