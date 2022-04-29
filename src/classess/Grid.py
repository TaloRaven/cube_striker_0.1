from functions.utlis import flatten_list
from colorama import Fore, init
init(autoreset=True)

class Grid:
    def __init__(self, list_of_cubes: [[]]):
        self.grid = list_of_cubes
        self.max_width = len(list_of_cubes[0])
        self.min_height = len(list_of_cubes)
        self.max_height = 0
        self.min_width = 0
        self.current_wave=0
        self.last_multiplier=0
        self.total_score=0
        self.last_score=0
    def display_grid(self, ):
        print(' ---------------------------------------------------------------------------------')
        for index, x in enumerate(self.grid):
            print(f'|   {x[0]}{x[1]}{x[2]}{x[3]}{x[4]}{x[5]}{x[6]}{x[7]}{x[8]}{x[9]}{x[10]}{x[11]}{x[12]}{x[13]}{x[14]}{x[15]}   |'
                  f'', flush=True)

            # print(f' {x[0]}{x[1]}{x[2]}{x[3]}')
        print(' ---------------------------------------------------------------------------------')
        print("type cube value, press enter to next wave or  /exit to quit game ")
    def group_grid_cube(self,group_number: int, coordinates: tuple):
        """group every element on grid """
        x, y = coordinates
        current_cube = self.grid[y][x]

        if current_cube.group != 'Empty':
            adjusted_points = current_cube.get_adjusted_cubes(self)

            adjusted_points_to_group = []
            for adj_point in adjusted_points:
                if adj_point['group'] is None:
                    if adj_point['value'] == current_cube.colour:
                        for row in self.grid:
                            for point in row:
                                if point.coordinates == adj_point['coordinates']:
                                    adjusted_points_to_group.append(adj_point['coordinates'])
            # TODO checmy dawac single ale narazie kazdemu elementowi jest przypisana grup[a nawet jak jest dsingle
            current_cube.group = group_number

        else:
            print('Empty element and we dont group him')

            # TODO W tym miejscu już mozemy generowac 'single' jesli roziwazemy pr
        if len(adjusted_points_to_group) == 0:
            if current_cube.group is None:
                current_cube.group = 'Single'
        else:
            for coordinate in adjusted_points_to_group:
                self.group_grid_cube(group_number=group_number,
                                coordinates=(coordinate[0], coordinate[1]))

        return self.grid

    def possible_moves(self) -> [()]:
        '''posible inputs you can make to break group of  blocks '''

        # coordinates = generate_grid_of_points(grid)
        t = 0

        while True:
            if t == 0:
                self.grid= self.group_grid_cube(t, (0, 0))
            else:
                self.grid = self.group_grid_cube(group_number=t,
                                           coordinates=(next_coordinates[0][0], next_coordinates[0][1]))

            next_coordinates = [[x.coordinates for x in y if x.group is None] for y in self.grid]

            next_coordinates = flatten_list(next_coordinates)

            if len(next_coordinates) != 0:
                t += 1
            else:
                grouped_points = flatten_list(self.grid)

                possible_groups = set([x.group for x in grouped_points if x.group != 'Empty'])

                groups = []
                for x in possible_groups:
                    group = []
                    for y in grouped_points:
                        if x == y.group:
                            group.append({'coordinates': y.coordinates, 'group': y.group})
                    groups.append(group)

                grouped_possible = [x for x in groups if len(x) > 1]
                grouped_possible = flatten_list(grouped_possible)

                # single_possible = [x for x in groups if len(x) == 1]
                # single_posible=flatten_list(single_posible)

                break
        return grouped_possible

    def score_break(self):
        self.last_score = (self.last_multiplier ** 2) * 10
        self.total_score=self.total_score+self.last_score

    def break_group(self, player_input: int) -> object:
        '''break possible group and remove it, evaluate mutlipier if group color was gold and update grid with gravity fall(
        every cube falls down untill hits ground or anather cube '''

        x = player_input // 10
        y = player_input % 10
        player_input=(x,y)


        possible_moves=self.possible_moves()
        ## Break chosen group if possible
        if player_input in [x['coordinates'] for x in possible_moves]:
            group_to_break = [x['group'] for x in possible_moves if x['coordinates'] == player_input]
            points_to_drop = [x['coordinates'] for x in possible_moves if x['group'] == group_to_break[0]]
            coordinates_to_drop = [[point for point in rows if point.coordinates in points_to_drop] for rows in self.grid]
            coordinates_to_drop = flatten_list(coordinates_to_drop)

            if coordinates_to_drop[0].colour==Fore.YELLOW:
                self.last_multiplier=len(coordinates_to_drop)
                self.score_break()

            # for rows in self.grid:
            #     for cube in rows:
            #         if cube.coordinates in [point.coordinates for point in coordinates_to_drop]:
            #             cube.colour = Fore.BLACK
            #             cube.group='Fall_Empty'
            # self.display_grid()
            # time.sleep(0.6)
            ## check how many blocks

            for rows in self.grid:
                for cube in rows:
                    if cube.coordinates in [point.coordinates for point in coordinates_to_drop]:
                        cube.colour = Fore.WHITE
                        cube.group='Fall_Empty'





            ## Fall
            ## check on withc column cube was borke
            columns_to_check = [[cube.coordinates[0] for cube in rows if cube.group == 'Fall_Empty'] for rows in self.grid]
            uniq_columns_to_check = set(flatten_list(columns_to_check))

            ## Extract columns with broken cubes
            grid_columns_to_fall = []
            for col_num, column in enumerate(uniq_columns_to_check):
                grid_column_to_fall = []
                for row_num, cube in enumerate(self.grid):
                    grid_column_to_fall.append(cube[column])
                grid_columns_to_fall.append(grid_column_to_fall)

            ## 'Gravity'- unbroken cubes falls down and empty cubes goes up in extracted columns
            new_colors = []
            for column_num, grid_column_to_fall in enumerate(grid_columns_to_fall):
                fall_empy_cubes = []
                rest_of_cubes = []
                for cube in grid_column_to_fall:
                    if cube.group == 'Fall_Empty':
                        fall_empy_cubes.append(cube.colour)
                    if cube.group != 'Fall_Empty':
                        rest_of_cubes.append(cube.colour)
                result = fall_empy_cubes + rest_of_cubes
                new_colors.append(result)
            ## with updated colors in extracted columns, change those columns in grid
            for col_num, column in enumerate(zip(uniq_columns_to_check, new_colors)):
                for row_num, cube in enumerate(self.grid):
                    cube[column[0]].colour = column[1][row_num]

            ## Reset groups
            for rows in self.grid:
                for cube in rows:
                    if cube.group!='Empty':
                        cube.group= None

            # TODO (chyba tos samo ) if in coordinates but no group single or empty (self.point.name cos tam ) jezeli nie ma na gridzie, invalid
        else:
            print('invalid input try again ')
            print(' Press coordinates x y example 00 56 12 14 etc. for element that has at least 1 adjusted cube with same color')
            print(' press /finish to quit game ')
        return self



    def __str__(self):
        return f"""{[print(row) for row in self.grid]}"""