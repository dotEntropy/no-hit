import pygame
from pygame import Surface
from pygame.mixer import Sound
from pygame.font import Font
from pygame.math import Vector2
import pathlib
from src.global_vars import GlobalVars


DEFAULT_SCALE = Vector2(1, 1)


def load_image(path: str, angle_deg: float=0, scale: Vector2=DEFAULT_SCALE) -> Surface:
    image = pygame.image.load(path).convert_alpha()
    image = modify_image(image, angle_deg=angle_deg, scale=scale)
    return image


def modify_image(image: Surface, angle_deg: float=0, scale: Vector2=DEFAULT_SCALE) -> Surface:
    scale_w = image.get_width() * scale.x
    scale_h = image.get_height() * scale.y
    if scale != DEFAULT_SCALE:
        image = pygame.transform.scale(image, (scale_w, scale_h))
    if angle_deg:
        image = pygame.transform.rotate(image, angle_deg)
    return image


ASSET_DIR = pathlib.Path(__file__).parent


def get_image(file_name: str, scale: Vector2=DEFAULT_SCALE) -> Surface:
    return load_image(ASSET_DIR / "gfx" / file_name, scale=scale)
    

def get_sound(file_name: str) -> Sound:
    return Sound(ASSET_DIR / "sfx" / file_name)


def get_font(file_name: str, size: int=20) -> Font:
    return Font(ASSET_DIR / "fonts" /file_name, size)
