import pygame

from pygame.locals import QUIT
from pygame.time import Clock

from Ball import Ball
from Player import Player


def handle_quit(events):
    # Quit event
    for event in events:
        if event.type is QUIT:
            pygame.quit()
            exit(0)


def main():
    # Init
    pygame.display.init()
    pygame.display.set_caption("TOTAL BREAKOUT")
    window = pygame.display.set_mode((1000, 800))
    info = pygame.display.Info()

    # Objects instanciation
    player = Player(info.current_w, info.current_h)
    ball = Ball(info.current_w, info.current_h)

    # Start screen
    pygame.font.init()
    myfont = pygame.font.SysFont("Comic Sans MS", 60)
    textsurface = myfont.render("PRESS SPACE", True, (255, 255, 255))
    window.blit(
        textsurface,
        (info.current_w / 2 - textsurface.get_width() / 2, info.current_h / 2),
    )
    pygame.display.flip()

    # Wait for user to start game
    while True:
        # Get keyboard events
        keys = pygame.key.get_pressed()

        # Handle quit event
        handle_quit(pygame.event.get())

        # Start game if SPACE is pressed
        if keys[pygame.K_SPACE]:
            break

    # Game main loop
    clock = Clock()
    is_running = True
    game_over = False
    while is_running:
        # Get keyboard events
        keys = pygame.key.get_pressed()

        # Handle quit event
        handle_quit(pygame.event.get())

        # Player controls
        dt = clock.tick(60)
        player.move(keys, dt)

        # Ball update
        game_over = ball.move(player, dt)

        # Draw
        window.fill((0, 0, 0))
        player.draw(window)
        ball.draw(window)
        pygame.display.flip()


if __name__ == "__main__":
    main()
