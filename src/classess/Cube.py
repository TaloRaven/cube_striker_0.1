"""One cube in wave """
from colorama import Fore, init
init(autoreset=True)

from classess.Grid import Grid

class Cube():
    """Represents single element in 16x 9y grid


     """
    def __init__(self, colour: str, coordinates: tuple, group=None) -> None:
        self.coordinates = coordinates
        self.colour=colour
        self.group = group
        self.x, self.y = self.coordinates
        self.height = self.y
        self.width = self.x

        #Empty(colour white),Single gr1,gr2...grn

    @property
    def coordinates(self) -> int:
        return self._coordinates

    @coordinates.setter
    def coordinates(self, value):
        self._coordinates = value

    def get_adjusted_cubes(self, grid:Grid) ->list:
        """If adjusted cube up, down, left or right meets conditon add it to adjusted points to group """
        # self.x, self.y = self.coordinates
        # self.height = self.y
        # self.width = self.x

        adjusted_points = []
        if self.height != grid.max_height:
            adjusted_points.append(
                {'name': 'up',
                 'value': grid.grid[self.y - 1][self.x].colour,
                 'coordinates': (self.x, self.y - 1),
                 'group': grid.grid[self.y - 1][self.x].group})

        if self.height != grid.min_height-1:
            adjusted_points.append(
                {'name': 'dwon',
                 'value': grid.grid[self.y + 1][self.x].colour,
                 'coordinates': (self.x, self.y + 1),
                 'group': grid.grid[self.y + 1][self.x].group})

        if self.width != grid.min_width:
            adjusted_points.append(
                {'name': 'left',
                 'value': grid.grid[self.y][self.x - 1].colour,
                 'coordinates': (self.x - 1, self.y),
                 'group': grid.grid[self.y][self.x - 1].group})
        if self.width != grid.max_width-1:
            adjusted_points.append(
                {'name': 'right',
                 'value': grid.grid[self.y][self.x + 1].colour,
                 'coordinates': (self.x + 1, self.y),
                 'group': grid.grid[self.y][self.x + 1].group})
        return adjusted_points

    # TODO testing display
    # def __str__(self):
    #     return f"""{self.colour}{  f'[{self.x}{self.y}]' if self.colour != Fore.WHITE  else ( str(f'    ') if self.x < 10 else str(f'     '))}"""

    def __str__(self):
        return f"""{f' {self.x}{self.y} ' if self.colour != Fore.WHITE  else ( str(f'[{0}{0}]') if self.x < 10 else str(f'[{0}{0}{0}]'))}"""