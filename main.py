"""Main function loop."""

from game import Game, Window, Particle
from pygame.color import Color
import random
import sys


# Declare constants
SCREEN_SIZE = Window(1280, 720)
SCREEN_COLOR = Color("#f5f5f5")
COLOR_PALETTE = [
    (194, 227, 236),
    (253, 243, 184),
    (251, 215, 183),
    (236, 180, 191),
    (198, 172, 199),
]
MAX_PARTICLES = 100
PARTICLE_SIZE = 25

# Store particles
particles = []


def game_logic(game: Game) -> None:
    """Any game logic."""
    # Capture any important events
    event = game.manager.event.poll()
    if event.type == game.manager.QUIT:
        # Quit game
        game.running = False

    # If the user clicks the mouse button
    if event.type == game.manager.MOUSEBUTTONDOWN:
        # Get the mouse position
        mouse_x, mouse_y = game.mouse_position

        # For the max range in particles
        for _ in range(MAX_PARTICLES):
            # Get a random color
            color = random.choice(COLOR_PALETTE)

            # Append a particle to the particles list
            particles.append(
                Particle(game, mouse_x, mouse_y, PARTICLE_SIZE, Color(*color))
            )

    # Update particles as needed.
    for particle in particles:
        particle.update()


def main():
    """Init function."""
    # Setup up logic
    with Game(SCREEN_SIZE, SCREEN_COLOR) as game:
        # Begin game loop
        game.init_loop(game_logic)


# Start it
main()
