from pygame.surface import Surface
from src.global_vars import GlobalVars
from src.parents.update_image import UpdateImage


class Bullet(UpdateImage):
    def __init__(self, IMAGE: Surface) -> None:
        super().__init__(IMAGE)

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
