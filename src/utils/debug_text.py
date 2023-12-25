import pygame
from pygame.math import Vector2
from src.global_vars import GlobalVars


class DebugText:
    def __init__(self) -> None:
        self.WIN = pygame.display.get_surface()
        self.font_size = int(24 * GlobalVars.sprite_scale.x)
        self.font = pygame.font.SysFont("Consolas", self.font_size)
        self.spacing = self.font.get_linesize() + 2
        self.texts = [] 
        self.total_ticks = 0
        self.POS = Vector2(20 * GlobalVars.sprite_scale.x, 20 * GlobalVars.sprite_scale.y)
    
    def update(self, texts: list=[], rate_ms: float=1):
        self.total_ticks = (self.total_ticks + 1) % rate_ms
        if self.total_ticks: return
        if type(texts) is list:
            self.texts = texts.copy()
            return
        self.texts = [texts]

    def draw(self) -> None:
        if not len(self.texts): return
        pos = self.POS.copy()
        for text in self.texts:
            surface = self.font.render(str(text), True, "white")
            self.WIN.blit(surface, pos)
            pos.y += self.spacing
