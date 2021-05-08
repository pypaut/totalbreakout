import pygame

from pygame.locals import QUIT
from pygame.time import Clock

from Ball import Ball
from Block import Block
from Player import Player


def handle_quit(events):
    # Quit event
    for event in events:
        if event.type is QUIT:
            pygame.quit()
            exit(0)


def start_screen(window, info):
    """
    Display starting screen
    """
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


def gameover_screen(window, info, clock):
    """
    Display game over screen
    """
    myfont = pygame.font.SysFont("Comic Sans MS", 60)
    textsurface = myfont.render(
        "GAME OVER ... PRESS SPACE", True, (255, 255, 255)
    )
    window.blit(
        textsurface,
        (info.current_w / 2 - textsurface.get_width() / 2, info.current_h / 2),
    )
    pygame.display.flip()

    # Wait for user to start game
    while True:
        # Clock ticks
        clock.tick(60)

        # Get keyboard events
        keys = pygame.key.get_pressed()

        # Handle quit event
        handle_quit(pygame.event.get())

        # Start game if SPACE is pressed
        if keys[pygame.K_SPACE]:
            break


def main():
    # Init
    pygame.display.init()
    pygame.font.init()
    pygame.display.set_caption("TOTAL BREAKOUT")
    window = pygame.display.set_mode((1000, 800))
    info = pygame.display.Info()

    # Objects instanciation
    player = Player(info.current_w, info.current_h)
    ball = Ball(info.current_w, info.current_h)
    blocks = []

    left_len = 10
    top_len = 5
    ext_block_size = info.current_w // left_len
    block_size = info.current_w // 40
    for i in range(left_len):
        for j in range(top_len):
            new_block = Block(
                block_size,
                i * ext_block_size,
                j * ext_block_size,
                info.current_w,
                info.current_h,
            )
            blocks.append(new_block)

    # Start screen
    start_screen(window, info)

    # Game main loop
    clock = Clock()
    is_running = True
    game_over = False
    while is_running:
        if game_over:
            gameover_screen(window, info, clock)
            ball.reset_pos()
            game_over = False

        # Get keyboard events
        keys = pygame.key.get_pressed()

        # Handle quit event
        handle_quit(pygame.event.get())

        # Player controls
        dt = clock.tick(60)
        player.move(keys, dt)

        # Ball update
        game_over = ball.move(player, blocks, dt)

        # Draw
        window.fill((0, 0, 0))
        for block in blocks:
            block.draw(window)
        player.draw(window)
        ball.draw(window)
        pygame.display.flip()


if __name__ == "__main__":
    main()
