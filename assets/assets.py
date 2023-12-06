import pygame
from pygame.math import Vector2
from pygame import Surface
from pygame.mixer import Sound
import pathlib


def load_image(path: str, angle_deg: float=0.0, scale: float=1.0) -> Surface:
    image = pygame.image.load(path).convert_alpha()
    scale_w = image.get_width() * scale
    scale_h = image.get_height() * scale
    if scale != 1:
        image = pygame.transform.scale(image, (scale_w, scale_h))
    if angle_deg:
        image = pygame.transform.rotate(image, angle_deg)
    return image


def modify_image(
        image: Surface, 
        angle_deg: float=0.0, 
        scale: Vector2=Vector2(1, 1)
        ) -> Surface:
    scaled_x = image.get_width() * scale.x
    scaled_y = image.get_height() * scale.y
    if scale != 1:
        image = pygame.transform.scale(image, (scaled_x, scaled_y))
    if angle_deg:
        image = pygame.transform.rotate(image, angle_deg)
    return image


ASSET_DIR = pathlib.Path(__file__).parent


def get_image(file_name: str) -> Surface:
    return load_image(ASSET_DIR / file_name)


def get_sound(file_name: str) -> Sound:
    return Sound(ASSET_DIR / file_name)
