"""Custom game class."""

from __future__ import annotations
from pygame.color import Color
from typing import List, Any, Tuple, Union
from .utils import Window
import pygame
import sys


class GameException(Exception):
    """Models a game exception."""


class Game(object):
    """Models a game class."""

    def __init__(self, window_size: Window, background_color: Color) -> None:
        """Init method."""
        self.manager = pygame
        self.draw = pygame.draw
        self.manager.init()
        self.clock = self.manager.time.Clock()
        self.running = True
        self.surface = self.manager.display.set_mode(window_size)
        self.background_color = background_color
        self.fill_window(self.background_color)
        self.render()

    def render(self) -> None:
        self.manager.display.flip()

    @property
    def events(self) -> List[Any]:
        """Return list of game events."""
        return self.manager.event.get()

    def __enter__(self) -> Game:
        """Enter dunder method."""
        return self

    def __exit__(
        self, exception_type: Any, exception_value: Any, traceback: Any
    ) -> None:
        """Exit dunder method."""
        # print(exception_type)
        # print(exception_value)
        # print(dir(traceback))
        # print(traceback.tb_frame)
        # print(traceback.tb_lasti)
        self.manager.quit()

    def fill_window(self, background_color: Color) -> None:
        self.surface.fill(background_color)

    def redraw_window(self) -> None:
        self.fill_window(self.background_color)
        self.manager.display.update()

    def init_loop(self, func: Callable) -> None:
        """Initialize the game loop."""
        while self.running:
            self.redraw_window()
            func(self)

    @property
    def mouse_position(self) -> Tuple[Union[float, int], Union[float, int]]:
        """Return the mouse position."""
        return self.manager.mouse.get_pos()

    def __repr__(self):
        """Representation method."""
        return f"{self.__class__.__name__}({self.manager})"
