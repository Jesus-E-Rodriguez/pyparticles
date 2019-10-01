"""Main function loop."""

from game import Game, Window, Particle
from pygame.color import Color
import sys

SCREEN_SIZE = Window(1280, 720)
SCREEN_COLOR = Color("red")

particles = []


def game_logic(game: Game) -> None:
    for event in game.events:
        if event.type == game.manager.QUIT:
            game.running = False

        if event.type == game.manager.MOUSEBUTTONDOWN:
            mouseX, mouseY = game.get_mouse_position()
            print(mouseX, mouseY)
            particles.append(Particle(mouseX, mouseY, 50, Color(0, 0, 0)))

        for particle in particles:
            particle.update(game)


def main():
    """Init function."""
    with Game(SCREEN_SIZE, SCREEN_COLOR) as game:
        game.init_loop(game_logic)

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
