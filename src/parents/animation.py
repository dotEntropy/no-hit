from src.parents.update_image import UpdateImage
from src.global_vars import GlobalVars


class Animation(UpdateImage):
    def __init__(self, asset_id: str, fps: int | float=1) -> None:
        self.fps = fps
        self.asset_id = asset_id
        self._load_frames()
    
    def _load_frames(self) -> None:
        self.frame_idx = 0
        self.frames = GlobalVars.get_asset(self.asset_id)
        self.frames = [self.frames] if type(self.frames) is not list else self.frames
        self.total_frames = len(self.frames)
        image = self.frames[int(self.frame_idx)]
        self._update_image(image)
    
    def _update_frames(self, asset_id: str, preserve_frame_idx: bool=False) -> None:
        if asset_id == self.asset_id: return
        if not preserve_frame_idx: self.frame_idx = 0
        self.asset_id = asset_id
        self.frames = GlobalVars.get_asset(self.asset_id)
        self.frames = [self.frames] if type(self.frames) is not list else self.frames
        self.total_frames = len(self.frames)
        image = self.frames[int(self.frame_idx)]
        self._update_image(image)

    def _update_animation(self) -> None:
        self.frame_idx = (self.frame_idx + self.fps * self.dt) % self.total_frames
        image = self.frames[int(self.frame_idx)]
        self._update_image(image)
        