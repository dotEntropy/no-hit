from pygame.math import Vector2

from config import *


class Globals:
    running = True
    client_w = 1920
    client_h = 1080
    bg_color = (20, 20, 20)
    fps = 300

    @staticmethod
    def get_sprite_scale() -> Vector2:
        scale_x = Globals.client_w / GAME_WIDTH
        scale_y = Globals.client_h / GAME_HEIGHT
        return Vector2(scale_x, scale_y)

    @staticmethod
    def get_center_pos() -> Vector2:
        return Vector2(Globals.client_w//2, Globals.client_h//2)

    @staticmethod
    def get_half_w() -> int:
        return Globals.client_w//2

    @staticmethod
    def get_half_h() -> int:
        return Globals.client_h//2
