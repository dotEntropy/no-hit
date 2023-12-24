from src.global_vars import GlobalVars
from src.parents.animation import Animation
from src.entities.player import Player


class Bullet(Animation):
    def __init__(self, asset_id: str) -> None:
        super().__init__(asset_id)
        self.is_projectile = True
        self.player_detect_range = 100
    
    def _detect_proximity(self, player: Player) -> None:
        if not self.is_projectile: 
            self._handle_collisions(player)
            return
        distance = self.pos.distance_to(player.pos)
        if distance > self.player_detect_range:
            self._update_frames("bloom-bullet-far")
            return
        self._update_frames("bloom-bullet-near")
        self._handle_collisions(player)
    
    def _handle_collisions(self, player: Player) -> None:
        if not self._collide_mask(self, player): return
        player.hp -= 1
        self.kill()

    def _update_pos(self, dt: float):
        self.pos += self.vel * dt
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
