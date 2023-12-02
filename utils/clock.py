from pygame.time import get_ticks
from typing import Callable


class Timer:
    def __init__(self, time_ms: int, func: Callable, loops: int=-1) -> None:
        """
        Specified function is called every specified milliseconds.\n
        Loops to infinity by default. Specify the amount of loops if needed.
        """
        self.time_ms = time_ms
        self.func = func
        self.loops_left = loops
        self.start_time = 0
        self.is_active = False

    def start(self) -> None:
        self.is_active = True
        self.start_time = get_ticks() 

    def stop(self) -> None:
        self.is_active = False
    
    def update(self) -> None:
        if not self.loops_left: return
        if not self.is_active: return
        if get_ticks() - self.start_time < self.time_ms: return
        self.start_time = get_ticks()
        if callable(self.func): self.func()
        if self.loops_left > 0: self.loops_left -= 1
