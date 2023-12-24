import pygame
from pygame import Surface
from pygame.mixer import Sound
from pygame.font import Font
from pygame.math import Vector2
import pathlib
import glob
import re
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
GFX_DIR = ASSET_DIR / "gfx"
SFX_DIR = ASSET_DIR / "sfx"
FONTS_DIR = ASSET_DIR / "fonts"


def get_image(file_name: str, scale: Vector2=DEFAULT_SCALE) -> Surface:
    try:
        return load_image(GFX_DIR / file_name, scale=scale)
    except FileNotFoundError:
        return load_image(GFX_DIR / "default.png")

def get_sound(file_name: str) -> Sound:
    return Sound(SFX_DIR / file_name)


def get_font(file_name: str, size: int=20) -> Font:
    return Font(FONTS_DIR / file_name, size)


def get_frames(file_name: str) -> list[Surface]:
    dot_idx = file_name.find(".")
    file_ext = file_name[dot_idx:]
    file_name = file_name[:dot_idx]

    pattern = f"{str(GFX_DIR)}\{file_name}-*{file_ext}"
    matching_files = glob.glob(pattern)
    if not matching_files:
        frame = get_image(f"{file_name}{file_ext}")
        return [frame]

    n_frames = len(matching_files)
    frames = [get_image(f"{file_name}-{i}{file_ext}") for i in range(n_frames)]
    return frames


class AssetClass:
    def load_assets(self) -> None:
        assets = {
            "player": get_frames("player.png"),
            "bloom-bullet-near": get_frames("bloom-bullet-near.png"),
            "bloom-bullet-far": get_frames("bloom-bullet-far.png"),
            "default": get_frames("default.png"),
            "icon": get_image("icon.png"),
        }
        GlobalVars.assets = assets
