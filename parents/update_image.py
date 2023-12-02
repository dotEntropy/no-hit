import pygame

from config import get_sprite_scale
from assets.assets import modify_image


class UpdateImage:
    def _update_image(self, image: pygame.Surface) -> None:
        self.image = modify_image(image, scale=get_sprite_scale())
        self.rect = self.image.get_rect(center=self.pos)