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


def wait(clock):
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


def start_screen(window, info, clock):
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
    wait(clock)


def win_screen(window, info, clock):
    """
    Display winning screen
    """
    myfont = pygame.font.SysFont("Comic Sans MS", 60)
    textsurface = myfont.render("YOU WIN! ... PRESS SPACE TO RESTART", True, (255, 255, 255))
    window.blit(
        textsurface,
        (info.current_w / 2 - textsurface.get_width() / 2, info.current_h / 2),
    )
    pygame.display.flip()

    # Wait for user to start game
    wait(clock)


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
    wait(clock)


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

    left_len = 20
    top_len = 8
    ext_block_size = info.current_w // left_len
    offset = 15 / 100 * ext_block_size
    block_size = ext_block_size - offset
    for i in range(1, left_len - 1):
        for j in range(1, top_len - 1):
            new_block = Block(
                block_size,
                i * ext_block_size + offset // 2,
                j * ext_block_size + offset // 2,
            )
            blocks.append(new_block)

    # Start screen
    clock = Clock()
    start_screen(window, info, clock)

    # Game main loop
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

        # Check if win
        if len(blocks) == 0:
            win_screen(window, info, clock)

        # Draw
        window.fill((0, 0, 0))
        for block in blocks:
            block.draw(window)
        player.draw(window)
        ball.draw(window)
        pygame.display.flip()


if __name__ == "__main__":
    main()
