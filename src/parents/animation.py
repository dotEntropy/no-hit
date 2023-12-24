from src.parents.update_image import UpdateImage
from src.global_vars import GlobalVars


class Animation(UpdateImage):
    def __init__(self, asset_id: str, fps: int | float=14) -> None:
        self.fps = fps
        self._update_frames(asset_id)
    
    def _update_frames(self, asset_id: str, preserve_frame_idx: bool=False) -> None:
        if not preserve_frame_idx: self.frame_idx = 0
        self.frames = GlobalVars.get_asset(asset_id)
        self.total_frames = len(self.frames)
        image = self.frames[int(self.frame_idx)]
        self._update_image(image)

    def _update_animation(self) -> None:
        image = self.frames[int(self.frame_idx)]
        self._update_image(image)
        self.frame_idx = (self.frame_idx + self.fps * self.dt) % self.total_frames
        