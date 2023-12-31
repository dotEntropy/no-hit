from pygame.time import get_ticks
from typing import Callable


class Timer:
    def __init__(
        self, 
        time_ms: int, 
        funcs: Callable | list[Callable], 
        loops: int=-1, 
        call_on_start: bool=True,
        **kwargs
        ) -> None:
        """
        Specified function is called every specified milliseconds.\n
        Loops to infinity by default. Specify the amount of loops if needed.\n
        Set param call_on_0 to False for function to not be called upon start.
        """
        self.time_ms = time_ms
        self.funcs = funcs
        self.kwargs = kwargs
        self.loops_left = loops
        self.start_time = 0
        self.is_active = False
        self.paused = False
        self.call_on_start = call_on_start

    def start(self) -> None:
        self.is_active = True
        self.start_time = get_ticks()
        
        if not self.call_on_start: return
        self._handle_function_calls()
        if self.is_infinite(): return
        self.loops_left -= 1

    def stop(self) -> None:
        self.is_active = False
    
    def toggle_active(self) -> None:
        self.is_active = not(self.is_active)

    def pause(self) -> None:
        self.pause = True
    
    def resume(self) -> None:
        self.pause = False
    
    def toggle_pause(self) -> None:
        self.paused = not(self.paused)

    def add_loops(self, amount: int) -> None:
        if self.is_infinite(): return
        self.loops_left += amount
    
    def change_interval(self, new_time_ms: int) -> None:
        self.time_ms = new_time_ms
    
    def is_infinite(self) -> None:
        if self.loops_left < 0:
            return True
        if self.loops_left > 0:
            return False
    
    def update(self) -> None:
        if not self.is_active: return
        if not self.loops_left: return
        if self.paused: self.start_time = get_ticks()
        if get_ticks() - self.start_time < self.time_ms: return
        self._handle_function_calls()
        self.start_time = get_ticks()
        if not self.is_infinite(): self.loops_left -= 1
    
    def _handle_function_calls(self) -> None:
        funcs = self.funcs
        if type(funcs) is not list:
            funcs = [funcs]
        for func in funcs:
            self._call_function(func)
    
    def _call_function(self, func) -> None:
        if not callable(func): return
        if self.kwargs:
            func(**self.kwargs)
            return
        func()
