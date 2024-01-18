import pygame
from pygame import Surface
from pygame.mixer import Sound
from pygame.font import Font
from pygame.math import Vector2
import pathlib
import os
import glob
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
GFX_DIR = ASSET_DIR / "images"
SFX_DIR = ASSET_DIR / "sounds"
FONTS_DIR = ASSET_DIR / "fonts"
assets = {}


def get_image(file_name: str, scale: Vector2=DEFAULT_SCALE) -> Surface:
    try:
        return load_image(GFX_DIR / file_name, scale=scale)
    except FileNotFoundError:
        return load_image(GFX_DIR / "default.png")

def get_sound(file_name: str) -> Sound:
    return Sound(SFX_DIR / file_name)


def get_font(file_name: str, size: int=20) -> Font:
    return Font(FONTS_DIR / file_name, size)


def load_assets() -> None:
    loop_files(ASSET_DIR)
    GlobalVars.assets = assets


def loop_files(target_dir) -> None:
    for file_name in os.listdir(target_dir):
        file_path = target_dir / file_name
        if os.path.isfile(file_path):
            add_asset(file_name)
        else:
            loop_files(file_path)


def add_asset(file_name: str) -> None:
    asset_id = os.path.splitext(file_name)[0]
    if is_image(file_name):
        assets[asset_id] = get_image(file_name)
        print(f"Loaded Asset: {file_name}")
    if is_sound(file_name):
        assets[asset_id] = get_sound(file_name)
        print(f"Loaded Asset: {file_name}")
    if is_font(file_name):
        assets[asset_id] = get_font(file_name)
        print(f"Loaded Asset: {file_name}")


def is_image(file_name: str) -> bool:
    conditions = (
        file_name.endswith(".png"),
    ) 
    return any(conditions)


def is_sound(file_name: str) -> bool:
    conditions = (
        file_name.endswith(".wav"),
        file_name.endswith(".mp3")
    ) 
    return any(conditions)


def is_font(file_name: str) -> bool:
    conditions = (
        file_name.endswith(".ttf"),
    ) 
    return any(conditions)
