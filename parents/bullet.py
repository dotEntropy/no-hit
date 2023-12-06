import pygame

from global_vars import Globals
from parents.update_image import UpdateImage


class Bullet(UpdateImage):
    def __init__(self, IMAGE: pygame.surface) -> None:
        super().__init__()
        self._update_image(IMAGE)

    def _update_pos(self, dt: float):
        self.pos += self.vel * dt
        self.rect.centerx = round(self.pos.x)
        self.rect.centery = round(self.pos.y)

    def _handle_despawn(self):
        border_w = Globals.client_w
        border_h = Globals.client_h
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
