from src.global_vars import GlobalVars
from src.parents.animation import Animation
from src.entities.player import Player


class Bullet(Animation):
    def __init__(self, asset_id: str) -> None:
        super().__init__(asset_id)
        self.is_projectile = True
        self.is_opaque = True
        self.player_detect_range = 100
    
    def _handle_collisions(self, player: Player) -> None:
        if not self.is_opaque: return
        if not self._collide_mask(self, player): return
        GlobalVars.game_over = True
        self.kill()

    def _update_pos(self):
        self.dt_vel = self.vel * self.dt
        self.dt_vel.x *= GlobalVars.sprite_scale.x
        self.dt_vel.y *= GlobalVars.sprite_scale.y
        self.pos += self.dt_vel
        self.rect.centerx = round(self.pos.x)
        self.rect.centery = round(self.pos.y)

    def _handle_despawn(self):
        border_w = GlobalVars.client_w
        border_h = GlobalVars.client_h
        offset_w = border_w * 0.2
        offset_h = border_h * 0.2
        kill_conditions = [
            self.pos.x < -offset_w,
            self.pos.x > border_w + offset_w,
            self.pos.y < -offset_h,
            self.pos.y > border_h + offset_h
        ]
        if any(kill_conditions):
            self.kill()
