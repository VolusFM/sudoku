from random import randrange

from numbers_set import NumbersSet
from sudoku_grid import SudokuGrid


class SudokuGridService(object):

    def create_complete_grid(self, grid_size) -> SudokuGrid:
        base: list[NumbersSet] = [NumbersSet(grid_size, [0 for _ in range(grid_size)]) for _ in range(grid_size)]
        grid: SudokuGrid = SudokuGrid(base)

        for line in range(grid_size):
            for column in range(grid_size):
                possible_numbers: list[int] = [_ for _ in range(1, grid_size + 1)]
                for delta_line in range(line):
                    for delta_column in range(column):
                        value: int = grid.lines[line - delta_line].numbers[column - delta_column]
                        if value in possible_numbers:
                            possible_numbers.remove(value)
                if len(possible_numbers) > 0:
                    index: int = randrange(0, len(possible_numbers), 1)
                    grid.lines[line].numbers[column] = possible_numbers[index]

        return grid
