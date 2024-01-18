from src.global_vars import GlobalVars
from src.parents.kinematics import Kinematics
from src.parents.animation import Animation
from src.entities.player import Player


class Bullet(Kinematics, Animation):
    def __init__(self, asset_id: str, total_frames: int=1) -> None:
        Kinematics.__init__(self)
        Animation.__init__(self, asset_id, total_frames=total_frames)
        self.is_projectile = True
        self.is_opaque = True
    
    def _handle_collisions(self, player: Player) -> None:
        if not self.is_opaque: return
        if not self._collide_mask(self, player): return
        GlobalVars.game_over = True
        self.kill()

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
