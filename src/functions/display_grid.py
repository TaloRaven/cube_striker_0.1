#!/usr/bin/env python3
from classess.Level import Level
from functions.utlis import cls, query_yes_no
from colorama import init, Fore

init(autoreset=True)
from colorama import init
import curses
from curses.textpad import Textbox, rectangle

init(autoreset=True)


def colours_to_values(grid):
    for rows in grid:
        for cube in rows:
            if cube.colour == Fore.WHITE:
                cube.value = 1
            elif cube.colour == Fore.RED:
                cube.value = 2
            elif cube.colour == Fore.GREEN:
                cube.value = 3
            elif cube.colour == Fore.BLUE:
                cube.value = 4
            elif cube.colour == Fore.YELLOW:
                cube.value = 5


def curses_init_color_pairs(stdscr):
    curses.start_color()

    stdscr = curses.initscr()
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_PAIRS, curses.COLOR_RED)
    curses.init_pair(3, curses.COLOR_PAIRS, curses.COLOR_MAGENTA)
    curses.init_pair(4, curses.COLOR_PAIRS, curses.COLOR_CYAN)
    curses.init_pair(5, curses.COLOR_PAIRS, curses.COLOR_YELLOW)


def post_round_msg(stdscr, lvl_num, level):
    stdscr.clear()
    stdscr.refresh()
    stdscr.addstr(10, 10, f"""
        Round {lvl_num}  COMPLITED 

        Total Score {level.grid.total_score}

        press any key to contiune""")

    stdscr.getkey()
    lvl_num = lvl_num + 1
    total_score = level.grid.total_score
    level = Level(lvl_num)
    level.grid.total_score = total_score
    game_state = 'active'
    stdscr.clear()
    stdscr.refresh()
    return game_state, lvl_num, level


def game_over_msg(stdscr, lvl_num: int, level: Level, game_state: str):
    stdscr.clear()
    stdscr.refresh()
    stdscr.addstr(10, 10, f"""
            Game Over

            Round {lvl_num}

            Total Score {level.grid.total_score}

    """)
    question = query_yes_no(stdscr, 'Play again ?')
    if question:
        game_state = 'active'
        lvl_num = 0
        level = Level(lvl_num)
    return game_state, level


def game_command(stdscr, player_input):
    if player_input == '/h ':
        stdscr.clear()
        stdscr.refresh()
        stdscr.addstr(10, 10, f'''

                  Goal of the game survive as long as you can
                  You can break cubes only if at least 2 of adjusted cubes are same color,
                  you get score for breaking yellow blocks,
                  you get no points from breaking anather colors 
                  you get -1 point for every break attempt 
                  the more adjusted yellow blocks are, the bigger score reward
                  Good luck !

                  commands /h- help

                  press any key to contiune 
                  ''')
        stdscr.clear()
        stdscr.refresh()
        stdscr.getkey()


def display_grid(stdscr, lvl_num, level, game_state):
    GRID_X = 10
    GRID_Y = 10
    # Last Score
    rectangle(stdscr, 5, 9, 8, 72)
    stdscr.addstr(6, 12,
                  f'Round {lvl_num + 1}        Last_Score: {level.grid.last_score}    gold multiplier: {level.grid.last_multiplier} ')
    stdscr.addstr(7, 12,
                  f'Wave {level.grid.current_wave} / {level.mine.mine_len}    Total Score: {level.grid.total_score} ')

    # Grid boarder
    rectangle(stdscr, 9, 9, 19, 80)

    ## display grid
    x_coordinates = [x for x in range(0, 40, 4)] + [y for y in range(40, 70, 5)]
    for column_index, x in enumerate(level.grid.grid):
        for index, x_coordinate in enumerate(x_coordinates):
            stdscr.addstr(column_index + GRID_Y, x_coordinate + GRID_X, str(f'{x[index]}'),
                          curses.color_pair(x[index].value))

    stdscr.refresh()
