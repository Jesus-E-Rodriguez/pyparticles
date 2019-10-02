"""Main Vector class."""

from __future__ import annotations
from typing import Union, Tuple, Dict
import math


class Vector(object):
    """Models a vector Vector(x, y)."""

    __slots__ = ["x", "y"]

    def __init__(
        self, x: Union[float, int] = 0, y: Union[float, int] = 0
    ) -> None:
        """Init method."""
        self.x = x
        self.y = y

    def set(self, vector: Vector) -> None:
        """Set current vector."""
        self.x, self.y = vector.x, vector.y

    def subtract(self, vector: Vector) -> None:
        """Subtract vector from current vector."""
        self.x -= vector.x
        self.y -= vector.y

    def add(self, vector: Vector) -> Vector:
        """Add a vector to the current vector."""
        self.x += vector.x
        self.y += vector.y
        return self

    def multiply(self, scalar: Union[float, int]) -> Vector:
        """Multiply vector by a scalar."""
        self.x *= scalar
        self.y *= scalar
        return self

    def divide(self, divisor: Union[float, int]) -> Vector:
        """Divide vector by divisor."""
        self.x /= divisor
        self.y /= divisor
        return self

    def copy(self) -> Vector:
        """Return a copy of the vector."""
        return Vector(self.x, self.y)

    @property
    def magnitude(self) -> float:
        """Calculate the length of the vector."""
        return math.sqrt(self.magnitude_squared)

    @property
    def magnitude_squared(self) -> float:
        """Calculate the squared magnitude of the vector."""
        return self.x ** 2 + self.y ** 2

    def set_magnitude(self, magnitude: Union[float, int]) -> Vector:
        """Set the magnitude of a vector."""
        return self.normalize().multiply(magnitude)

    def normalize(self) -> Vector:
        """Normalize the vector to length 1 (make it a unit vector)."""
        return self if self.magnitude == 0 else self.divide(self.magnitude)

    def get_vector_from_angle(self, angle) -> Vector:
        """Return a vector from an angle in radians."""
        return Vector(math.cos(angle), math.sin(angle))

    def limit(self, max_limit: Union[float, int]) -> Vector:
        """Limit the magnitude given a max limit."""
        magnitude_squared = self.magnitude_squared
        if magnitude_squared > max_limit ** 2:
            self.divide(math.sqrt(magnitude_squared)).multiply(max_limit)
        return self

    def __repr__(self) -> str:
        """Return a nicely formatted representation string."""
        return f"{self.__class__.__name__}(x={self.x!r}, y={self.y!r})"

    @property
    def direction(self) -> Union[float, int]:
        """Return the direction of the vector."""
        return math.atan2(self.y, self.y)

    @property
    def to_dict(self) -> Dict[str, Union[float, int]]:
        """Return a new OrderedDict which maps field names to their values."""
        return {"x": self.x, "y": self.y}

    @property
    def to_tuple(self) -> Tuple[Union[float, int], Union[float, int]]:
        """Return a tuple."""
        return (self.x, self.y)
