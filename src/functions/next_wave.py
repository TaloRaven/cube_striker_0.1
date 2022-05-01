#!/usr/bin/env python3
from typing import Union

from classess.Level import Level
from colorama import Fore, init

init(autoreset=True)


def next_wave(level: Level, game_state: 'str') -> tuple[Union[Level, Level], str]:
    """for current level  move 1 column of cubes from mine to grid """
    # TODO
    # jezeli waveow jest za duzo to sie sypie
    # tutaj warunek stopu
    level.grid.current_wave += 1
    if level.grid.grid[-1][-1].colour != Fore.WHITE:
        game_state = 'game_over'

    last_row = level.grid.grid[-1]
    grid_index_pop_column = -1
    for index, cube in enumerate(last_row):
        if cube.colour == Fore.WHITE:
            if index == 0:
                grid_index_pop_column = 0
                break
            elif index >= 1 and index != len(last_row):
                if last_row[index - 1].colour != Fore.WHITE:
                    grid_index_pop_column = index
                break
            else:
                continue

    # Replace empty column with new wave from mine to grid
    try:
        for index, element in enumerate(level.mine.mine):
            last_dropped_column = level.grid.grid[index].pop(grid_index_pop_column)
            level.grid.grid[index].insert(0, element[-1])
            level.mine.mine[index].pop()

        if last_dropped_column.colour != Fore.WHITE:
            game_state = 'game_over'

            # reset coordinates
        for y in range(0, level.grid.min_height):
            for x in range(0, level.grid.max_width):
                level.grid.grid[y][x].coordinates = (x, y)
                level.grid.grid[y][x].x = x
                level.grid.grid[y][x].y = y
                level.grid.grid[y][x].width = x
                level.grid.grid[y][x].height = y
    except:
        game_state = 'level_completed'

    return level, game_state
