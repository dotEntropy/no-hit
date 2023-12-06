import pygame

from global_vars import Globals
from assets.assets import modify_image


class UpdateImage:
    def _update_image(self, image: pygame.Surface) -> None:
        self.image = modify_image(image, scale=Globals.get_sprite_scale())
        self.rect = self.image.get_rect(center=self.pos)
