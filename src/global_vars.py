from pygame.math import Vector2
from pygame.surface import Surface


class GlobalVars:
    GAME_W = 1920
    GAME_H = 1080
    DEFAULT_BG_COLOR = [30, 30, 30]
    client_w = 1920
    client_h = 1080
    bg_color = DEFAULT_BG_COLOR.copy()
    fps = 300
    sprite_scale = 1
    states = {}
    active_state = None
    assets = {}

    @staticmethod
    def get_center_pos() -> Vector2:
        return Vector2(GlobalVars.client_w, GlobalVars.client_h) // 2
    
    def get_asset(asset_id: str, is_image=True) -> Surface:
        if is_image:
            return GlobalVars.assets.get(asset_id, GlobalVars.assets["default"])
        return GlobalVars.assets.get(asset_id)

    def _update_sprite_scale() -> None:
        w_ratio = GlobalVars.client_w / GlobalVars.GAME_W
        h_ratio = GlobalVars.client_h / GlobalVars.GAME_H
        GlobalVars.sprite_scale = Vector2(w_ratio, h_ratio)