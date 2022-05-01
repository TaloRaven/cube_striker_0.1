#!/usr/bin/env python3

from colorama import init
from curses import wrapper

init(autoreset=True)

from classess.Level import Level
from functions.player_input import *
from functions.display_grid import *


def cube_strike(stdscr):
    curses_init_color_pairs(stdscr)
    game_command(stdscr, player_input='/h')

    lvl_num = 0
    level = Level(lvl_num)
    game_state = 'active'
    stdscr.clear()
    stdscr.refresh()

    while game_state == 'active':
        colours_to_values(level.grid.grid)

        display_grid(stdscr, lvl_num, level, game_state)

        level, game_state = player_input(stdscr, level, game_state)

        if game_state == 'level_completed':
            game_state, lvl_num, level = post_round_msg(stdscr, lvl_num, level)

        if game_state == 'game_over':
            game_state, level = game_over_msg(stdscr, lvl_num, level, game_state)


if __name__ == "__main__":
    wrapper(cube_strike)
