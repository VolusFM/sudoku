from random import randrange

from sudoku_grid import SudokuGrid
from sudoku_grid_display_service import SudokuGridDisplayService


class SudokuGridService(object):

    def create_complete_grid(self, grid_size) -> SudokuGrid:
        base: list[list[int]] = [[0 for _ in range(grid_size)] for _ in range(grid_size)]
        grid: SudokuGrid = SudokuGrid(base)

        for line in range(grid_size):
            for column in range(grid_size):
                zone: int = (line // grid.zone_size) * grid.zone_size + column // grid.zone_size
                possible_numbers: list[int] = [_ for _ in range(1, grid_size + 1)
                                               if _ not in grid.extract_line(line)
                                               and _ not in grid.extract_column(column)
                                               and _ not in grid.extract_zone(zone)]

                if len(possible_numbers) > 0:
                    index: int = randrange(0, len(possible_numbers), 1)
                    grid.lines[line][column] = possible_numbers[index]

        return grid
