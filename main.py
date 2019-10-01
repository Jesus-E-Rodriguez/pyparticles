"""Main function loop."""

from game import Game
from pygame.color import Color
from utils import Window
import pygame
import sys

SCREEN_SIZE = Window(1280, 720)
SCREEN_COLOR = Color("red")


def main():
    """Init function."""
    with Game(SCREEN_SIZE, SCREEN_COLOR) as game:
        while True:
            for event in game.events:
                print(event)

            #      if e.type == pg.MOUSEBUTTONDOWN:
            # (mouseX, mouseY) = pg.mouse.get_pos()
    # screen = pygame.display.set_mode(SCREEN_SIZE)
    # print(SCREEN_COLOR)
    # print(type(SCREEN_COLOR))
    # screen.fill(SCREEN_COLOR)
    # screen.display.flip()
    # while True:
    #     for events in pygame.event.get():
    #         print(type(pygame.event.get()))
    #         if events.type == pygame.QUIT:
    #             sys.exit(0)


main()
