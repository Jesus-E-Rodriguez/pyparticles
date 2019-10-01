"""Collection of utilities."""

from collections import namedtuple

Color = namedtuple(
    "Color", ["red", "green", "blue", "alpha"], defaults=[0, 0, 0, 1]
)
Window = namedtuple("Window", ["width", "height"])
