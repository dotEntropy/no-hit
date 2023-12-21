from pygame.math import Vector2
from src.global_vars import GlobalVars
from src.assets import assets


class Camera:
    def handle_camera_pan(self, drag_offset: Vector2) -> None:
        if not self.is_dragging:
            self.drag_pos = self.pos
            self.is_dragging = True
        self.pos = self.drag_pos + drag_offset
    