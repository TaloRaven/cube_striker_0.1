#!/usr/bin/env python3
from src.classess.Grid import Grid
from src.classess.Mine import Mine
from src.classess.Cube import Cube
from src.classess.Level import Level
from random import randint, choice

from colorama import Fore, init

init(autoreset=True)


def generate_level(lvl_number: int, width: int, height: int) -> Level:
    """based on current lvl generate Mine and playable Grid"""
    ## Mine is random generated set of cubes in table, width depend on current level

    # Possible cube types White(Empty), Green, Red, Blue, Gold(Yellow)
    possible_cube_colors = [Fore.RED, Fore.GREEN, Fore.BLUE, Fore.YELLOW]
    mine = Mine([[Cube(choice(possible_cube_colors), (x, y)) for x in range(0, width)] for y in range(0, height)],lvl_number)


    #TODO juz ustawic na flast 16 9 dlugosc
    grid = Grid([[Cube(Fore.WHITE, (x, y), group='Empty') for x in range(0, 16)] for y in range(0, 9)])

    return Level(mine, grid)
