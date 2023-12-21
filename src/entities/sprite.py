from pygame.sprite import Sprite
from pygame.math import Vector2
from src.assets import assets
from src.utils import vectors
from src.global_vars import GlobalVars


class Object(Sprite):
    def __init__(self, pos: Vector2) -> None:
        super().__init__()

        self.pos = pos
        self.IMAGE = assets.get_image("object.png")
        self.image = self.IMAGE
        self.rect = self.image.get_rect(topleft=self.pos)
    
    def update(self, dt: float) -> None:
        self.dt = dt
        self._update_pos()
    
    def _update_pos(self) -> None:
        self.rect.topleft = [round(self.pos.x), round(self.pos.y)]
    