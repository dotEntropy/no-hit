import pygame
from pygame.math import Vector2


class DebugText:
    def __init__(self) -> None:
        self.WIN = pygame.display.get_surface()
        self.font = pygame.font.SysFont("Consolas", 24)
        self.spacing = self.font.get_linesize() + 2
        self.texts = [] 

    def draw(self) -> None:
        if not self.texts: return
        if type(self.texts) is not list:
            self.texts = [self.texts]
        pos = Vector2(20, 20)
        for text in self.texts:
            surface = self.font.render(str(text), True, "white")
            self.WIN.blit(surface, pos)
            pos.y += self.spacing
        pos.y = 20
