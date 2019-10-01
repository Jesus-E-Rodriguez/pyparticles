"""Main particle class."""

from .game import Game
from .vector import Vector
from pygame.color import Color
from typing import Union
import random


class Particle:
    """Models a particle."""

    def __init__(
        self,
        x: Union[float, int],
        y: Union[float, int],
        size: Union[float, int],
        color: Color,
    ) -> None:
        """Init method."""
        self.position = Vector(x, y)
        self.previous = Vector(x, y)
        self.velocity = Vector(random.randint(0, 99), random.randint(0, 99))
        self.acceleration = Vector()
        self.size = size
        self.color = color

    def update(self, game: Game) -> None:
        """Update particle's position."""
        self.velocity.add(self.acceleration)
        self.velocity.limit(5)
        self.position.add(self.velocity)
        self.acceleration.multiply(0)
        self.draw(game)

    def draw(self, game: Game) -> None:
        """Draw particle."""
        print(self.position)
        print(self.position.to_tuple)
        print("here")
        game.draw.circle(
            game.surface,
            self.color,
            (int(self.position.x), int(self.position.y)),
            self.size,
        )
        game.render()
