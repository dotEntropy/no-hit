from pygame.math import Vector2


GAME_WIDTH = 1920
GAME_HEIGHT = 1080
client_w = 1920
client_h = 1080
FPS = 0  # 0 for unlimited 


def get_sprite_scale() -> float:
    game_ratio = GAME_WIDTH / GAME_HEIGHT
    client_ratio = client_w / client_h
    if game_ratio != client_ratio: return
    return client_w / GAME_WIDTH


def get_center_pos() -> Vector2:
    return Vector2(client_w//2, client_h//2).copy()


def get_hf_width() -> int:
    return client_w//2


def get_hf_height() -> int:
    return client_h//2