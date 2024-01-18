from pygame.math import Vector2
from src.global_vars import GlobalVars


class Kinematics:
    def __init__(self) -> None:
        self.pos = Vector2(GlobalVars.get_center_pos())
        self.vel = Vector2()
        self.dt_vel = Vector2()
        self.accel = Vector2()
        self.force = Vector2()

    def _update_pos(self) -> None:
        if not self.vel: return
        self.dt_vel = self.vel * self.dt
        if not self.dt_vel: return
        self.dt_vel.x *= GlobalVars.sprite_scale.x
        self.dt_vel.y *= GlobalVars.sprite_scale.y
        self.pos += self.dt_vel
        self.rect.centerx = round(self.pos.x)
        self.rect.centery = round(self.pos.y)
