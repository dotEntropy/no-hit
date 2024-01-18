from src.parents.update_image import UpdateImage
from src.global_vars import GlobalVars


class Animation(UpdateImage):
    def __init__(self, asset_id: str, total_frames: int=1, fps: int | float=1) -> None:
        self.asset_id = None
        self._update_frames(asset_id, total_frames, fps)
    
    def _update_frames(
            self, 
            asset_id: str, 
            total_frames: int=1, 
            fps: int | float=1, 
            preserve_frame_idx: bool=False
            ) -> None:
        if asset_id == self.asset_id: return
        if not preserve_frame_idx: self.frame_idx = 0
        self.asset_id = asset_id
        self.total_frames = total_frames
        self.fps = fps
        self.frames = []
        if self.total_frames == 1:
            self.frames = [GlobalVars.get_asset(self.asset_id)]
        else:
            self._load_frames()
        self._update_current_image()
    
    def _load_frames(self) -> None:
        for i in range(self.total_frames):
            frame = GlobalVars.get_asset(f"{self.asset_id}-{i}")
            self.frames.append(frame)

    def _update_animation(self) -> None:
        self.frame_idx = (self.frame_idx + self.fps * self.dt) % self.total_frames
        self._update_current_image()
    
    def _update_current_image(self) -> None:
        current_image = self.frames[int(self.frame_idx)]
        self._update_image(current_image)
        