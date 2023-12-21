from pygame.math import Vector2
from pygame.surface import Surface
from src.global_vars import GlobalVars
from src.assets.assets import modify_image


class UpdateImage:
    def __init__(self, IMAGE: Surface) -> None:
        self.IMAGE = IMAGE
        self._update_sprite_scale()
        self._update_image()

    def _update_image(self) -> None:
        self.image = modify_image(self.IMAGE, scale=GlobalVars.sprite_scale)
        self.rect = self.image.get_rect(center=self.pos)
    
    def _update_sprite_scale(self) -> None:
        w_ratio = GlobalVars.client_w / GlobalVars.GAME_W
        h_ratio = GlobalVars.client_h / GlobalVars.GAME_H
        GlobalVars.sprite_scale = Vector2(w_ratio, h_ratio)
