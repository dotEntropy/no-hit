from pygame import mask
from pygame.math import Vector2
from pygame.surface import Surface
from src.global_vars import GlobalVars
from src.assets.assets import modify_image


class UpdateImage:
    def __init__(self, IMAGE: Surface) -> None:
        self.IMAGE = IMAGE
        self._update_image(IMAGE)

    def _update_image(self, new_image: Surface) -> None:
        self.image = modify_image(new_image, scale=GlobalVars.sprite_scale)
        self.rect = self.image.get_rect(center=self.pos)
        self.mask = mask.from_surface(self.image)
    
    @staticmethod
    def _collide_mask(sprite_a, sprite_b):
        rect_collision = sprite_a.rect.colliderect(sprite_b.rect)
        offset = (sprite_b.rect.x - sprite_a.rect.x, sprite_b.rect.y - sprite_a.rect.y)
        mask_collision = sprite_a.mask.overlap(sprite_b.mask, offset)
        return rect_collision and mask_collision
