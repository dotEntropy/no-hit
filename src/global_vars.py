from pygame.math import Vector2


class GlobalVars:
    GAME_W = 1920
    GAME_H = 1080
    DEFAULT_BG_COLOR = [30, 30, 30]
    client_w = 1920
    client_h = 1080
    bg_color = DEFAULT_BG_COLOR.copy()
    fps = 0
    w_ratio = client_w / GAME_W
    h_ratio = client_h / GAME_H
    sprite_scale = Vector2(w_ratio, h_ratio)
    states = {}
    active_state = None

    @staticmethod
    def get_center_pos() -> Vector2:
        return Vector2(GlobalVars.client_w, GlobalVars.client_h) // 2
