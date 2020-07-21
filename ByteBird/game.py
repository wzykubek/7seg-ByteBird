#!/usr/bin/env python3

from ZeroSeg import Button, screen
from time import sleep
from random import randrange
from threading import Thread
import sys

right_button = Button("right")
left_button = Button("left")


def generate_hurdle() -> int:
    """
    Generate random number (0 or 1) and because of it create obstacle
    on the top of the map or on the bottom.
    """
    rand = randrange(2)

    if rand == 1:
        return 35  # Top hurdle (stalactite).
    else:
        return 29  # Bottom hurdle.


class ctx(object):
    """
    Game context.
    """

    if len(sys.argv) > 1:
        difficulty = float(sys.argv[1])
    else:
        difficulty = 0.3  # More == easier.

    hero_up = 64
    hero_down = 8
    hero_position = hero_down
    hero_index = 6

    hurdles = [generate_hurdle(), generate_hurdle()]
    points = 0
    game = True


def game_over():
    """
    Display game over screen.
    """
    ctx.game = False
    screen.write_blinking_text("  LOSE  ", stop_after=2)
    screen.write_text(f"P {ctx.points}")


def draw_hurdles(hurdles_byte: int, position: int):
    """
    Simple wrapper function to draw hurdles.
    """
    screen.set_byte(hurdles_byte, position)


def draw_hero(position: int, hurdle: int = False) -> bool:
    """
    Draw a hero on the screen on specified position. If hero is in a clash
    with hurdle, draw hero under or over it.
    """
    if hurdle:  # Draw hero over or under obstacle.
        if position == ctx.hero_down and hurdle == 35:
            screen.set_byte(43, ctx.hero_index)  # 43 - hero under obstacle.
        elif position == ctx.hero_up and hurdle == 29:
            screen.set_byte(93, ctx.hero_index)  # 93 - hero over obstacle.
        else:
            game_over()
            return False
    else:
        screen.set_byte(position, ctx.hero_index)
    return True


def handle_movements():
    """
    Handle button presses in other thread.
    """
    while ctx.game:
        if right_button.pressed():
            ctx.hero_position = ctx.hero_up
        elif left_button.pressed():
            ctx.hero_position = ctx.hero_down


def main():
    screen.write_blinking_text(' ' + '.'*5, stop_after=2)
    Thread(target=handle_movements, daemon=True).start()
    i = 1

    while True:
        screen.clear()

        if i > 8:
            i = 1
            del ctx.hurdles[0]
            ctx.hurdles.append(generate_hurdle())
            ctx.points += 1

        if i != ctx.hero_index:
            draw_hurdles(ctx.hurdles[0], i)

        draw_hero(ctx.hero_position)  # Restore hero on previous position.

        if i >= 4:
            draw_hurdles(ctx.hurdles[1], i - 3)
            if i == ctx.hero_index:
                if not (draw_hero(ctx.hero_position, ctx.hurdles[0])):
                    break

        if ctx.points > 0:
            if i < 4:
                if (ctx.hero_index - 1) + i == ctx.hero_index:
                    if not (draw_hero(ctx.hero_position, ctx.hurdles[0])):
                        break
                else:
                    draw_hurdles(ctx.hurdles[0], (ctx.hero_index - 1) + i)

        i += 1
        sleep(ctx.difficulty)


if __name__ == "__main__":
    main()
