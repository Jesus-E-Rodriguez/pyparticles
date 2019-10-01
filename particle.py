"""Main particle class."""

from pygame.math import Vector2 as Vector
from typing import Union
from random import random


class Particle:
    """Models a particle."""

    def __init__(
        self,
        x: Union[float, int],
        y: Union[float, int],
        size: Union[float, int],
        color: str,
    ) -> None:
        """Init method."""
        self.position = Vector(x, y)
        self.previous = Vector(x, y)
        self.velocity = Vector(random(), random())
        self.acceleration = Vector()
        self.size = size
        self.color = color

    def update(self) -> None:
        """Update particle's position."""
        self.velocity.add(self.acceleration)
        self.velocity.limit(5)
        self.position.add(self.velocity)
        self.acceleration.mult(0)
        self.draw()

    def draw(self) -> None:
        """Draw particle."""
        pass
