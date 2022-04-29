from classess.Grid import Grid
from classess.Mine import Mine
from classess.Cube import Cube
from random import randint, choice

from colorama import Fore, init

class Level():

    def __init__(self,level_number: int):
        self.level_number=level_number
        self.possible_cube_colors = [Fore.RED, Fore.GREEN, Fore.BLUE, Fore.YELLOW]
        self.mine=Mine([[Cube(choice(self.possible_cube_colors), (x, y)) for x in range(0, 18 + 4 * self.level_number)] for y in range(0, 9)],self.level_number)
        self.grid=Grid([[Cube(Fore.WHITE, (x, y), group='Empty') for x in range(0, 16)] for y in range(0, 9)])


