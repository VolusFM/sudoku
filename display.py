import os

from numbers_set import NumbersSet
from sudoku_grid import SudokuGrid


zone_separator: str = '|'


def display(grid: SudokuGrid) -> None: # TODO convert to service
    # TODO refactor this into a method
    top_line: str = ('+' + '-' * (2 * grid.zone_size + 1)) * grid.zone_size + '+'
    zones_group_separator: str = ('|' + '-' * (2 * grid.zone_size + 1)) * grid.zone_size + '|'

    grid_display: str = f'{os.linesep}{top_line}{os.linesep}'

    i: int = 0
    for line in grid.lines:
        i += 1
        grid_display = f'{grid_display}{zone_separator} {get_line_to_display(line, grid.zone_size)}'
        if i % grid.zone_size == 0 and i < grid.size:
            grid_display = f'{grid_display}{os.linesep}{zones_group_separator}'
        grid_display = f'{grid_display}{os.linesep}'

    grid_display = f'{grid_display}{top_line}'
    print(grid_display)


def get_line_to_display(line: NumbersSet, zone_size: int) -> str:
    i: int = 0
    line_to_display: str = ''

    for number in line:
        i += 1
        line_to_display = f'{line_to_display}{number} '
        if i == zone_size:
            line_to_display = f'{line_to_display}{zone_separator} '
            i = 0

    return line_to_display.replace('0', '_')
