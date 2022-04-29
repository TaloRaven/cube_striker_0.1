from src.classess.Cube import Cube
class Mine:
    def __init__(self, list_of_cubes: [[Cube]], lvl: int):
        self.mine=list_of_cubes
        self.mine_lvl=lvl
        self.mine_len = 18 + 4 * self.mine_lvl
        self.mine_width=len(list_of_cubes[0]) - 1
        self.mine_height=len(list_of_cubes) - 1

    def __str__(self):
        return f"""{[print(row) for row in self.mine]}"""