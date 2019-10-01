"""Custom game class."""

from __future__ import annotations
from pygame.color import Color
from typing import List, Any, Sequence
from utils import Window
import pygame
import sys


class GameException(Exception):
    """Models a game exception."""


class Game(object):
    """Models a game class."""

    def __init__(self, window_size: Window, background_color: Color) -> None:
        """Init method."""
        self.manager = pygame
        self.manager.init()
        self.clock = self.manager.time.Clock()
        self.running = True
        self.window_size = window_size
        self.background_color = background_color
        self.window = self.manager.display.set_mode(window_size)
        self.window.fill(background_color)
        self.manager.display.flip()

    @property
    def events(self) -> Events:
        """Return list of game events."""
        yield Events(self.manager.event.get())

    def __enter__(self) -> Game:
        """Enter dunder method."""

        return self

    def __exit__(self, type: Any, value: Any, traceback: Any) -> None:
        """Exit dunder method."""
        print(args)
        print(kwargs)
        if event.type == pygame.QUIT:
            sys.exit(0)

    def __repr__(self):
        """Representation method."""
        return f"{self.__class__.__name__}({self.game})"


class Events(object):
    """Models an event stream."""

    def __init__(self, events: List[Any]) -> None:
        """Init method."""
        self.events = events

    def __len__(self) -> int:
        """Length method."""
        return len(self.events)

    def __getitem__(self, index: int) -> Any:
        """Get item method."""
        if index >= len(self):
            raise IndexError
        return self[index]
