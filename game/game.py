"""Custom game class."""

from __future__ import annotations
from pygame.color import Color
from typing import List, Any, Tuple, Union, Callable
from .utils import Window
import pygame
import sys


# Wrapper game class, for ease of use
class Game(object):
    """Models a game class."""

    def __init__(self, window_size: Window, background_color: Color) -> None:
        """Init method."""
        self.manager = pygame
        self.draw = pygame.draw
        self.manager.init()
        self.running = True
        self.surface = self.manager.display.set_mode(window_size)
        self.background_color = background_color
        self.fill_window(self.background_color)
        self.render()

    def __enter__(self) -> Game:
        """Enter dunder method."""
        return self

    def __exit__(
        self, exception_type: Any, exception_value: Any, traceback: Any
    ) -> None:
        """Exit dunder method."""
        self.manager.quit()

    def render(self) -> None:
        """Render method."""
        self.manager.display.update()

    def fill_window(self, background_color: Color) -> None:
        """Fill the window surface."""
        self.surface.fill(background_color)

    def redraw_window(self) -> None:
        """Redraw the window as needed."""
        self.fill_window(self.background_color)

    def init_loop(self, function: Callable) -> None:
        """Initialize the game loop."""
        # While the game is running, redraw/clear the window
        # Run any custom game logic
        # Render out to screen
        while self.running:
            self.redraw_window()
            function(self)
            self.render()

    @property
    def mouse_position(self) -> Tuple[Union[float, int], Union[float, int]]:
        """Return the mouse position."""
        return self.manager.mouse.get_pos()

    def __repr__(self):
        """Representation method."""
        return f"{self.__class__.__name__}({self.manager.__class__.__name__})"
