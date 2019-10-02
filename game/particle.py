"""Main particle class."""

from pygame.color import Color
from .vector import Vector
from typing import Union
from .game import Game
import random


class Particle:
    """Models a particle."""

    def __init__(
        self,
        game: Game,
        x: Union[float, int],
        y: Union[float, int],
        size: Union[float, int],
        color: Color,
    ) -> None:
        """Init method."""
        self.game = game
        self.position = Vector(x, y)
        self.velocity = Vector(
            random.randint(-99, 99), random.randint(-99, 99)
        )
        self.acceleration = Vector()
        self.size = size
        self.color = color
        self.screen_width, self.screen_height = (
            self.game.manager.display.get_surface().get_size()
        )

    def update(self) -> None:
        """Update particle's position."""
        self.velocity.add(self.acceleration)
        self.velocity.limit(5)
        self.position.add(self.velocity)
        self.acceleration.multiply(0)
        self.draw()
        self.bound()

    def draw(self) -> None:
        """Draw particle."""
        self.game.draw.circle(
            self.game.surface,
            self.color,
            (int(self.position.x), int(self.position.y)),
            self.size,
        )

    def bound(self) -> None:
        """Bound object to screen."""
        # If the particle touches the screen boundary, then reverse its velocity
        if (
            self.position.x - self.size <= 0
            or self.position.x + self.size >= self.screen_width
        ):
            self.velocity.x = -self.velocity.x

        if (
            self.position.y - self.size <= 0
            or self.position.y + self.size >= self.screen_height
        ):
            self.velocity.y = -self.velocity.y
