from typing import Callable

import numpy as np

from numbers_set import NumbersSet


class SudokuGrid(object):
    zone_size: int
    size: int
    lines: list[NumbersSet]

    def __init__(self, lines: list[list[int]]):
        if len(lines) == 0 or len(lines[0]) == 0:
            raise

        self.size = len(lines[0])
        self.zone_size: int = int(np.sqrt(self.size))  # TODO repurpose this to handle non-square grids
        self.lines = []

        for line in lines:
            if len(line) != self.size:
                raise
            self.lines.append(NumbersSet(self.size, line))

    def extract_line(self, index) -> NumbersSet:
        if index > self.size:
            raise

        return self.lines[index]

    def extract_column(self, index) -> NumbersSet:
        col: list[int] = []
        for line in self.lines:
            col.append(line[index])

        return NumbersSet(self.size, col)

    def extract_zone(self, index) -> NumbersSet:
        zone: list[int] = []
        zone_line_index: int = index // self.zone_size
        zone_column_index: int = index % self.zone_size

        for line in range(self.zone_size):
            for column in range(self.zone_size):
                zone.append(self.lines
                            [self.zone_size * zone_line_index + line]
                            [self.zone_size * zone_column_index + column])

        return NumbersSet(self.size, zone)

    def is_complete(self) -> bool:
        return self.apply_predicate_to_grid(NumbersSet.is_complete)

    def is_correct(self) -> bool:
        return self.apply_predicate_to_grid(NumbersSet.is_correct)

    def apply_predicate_to_grid(self, predicate: Callable[[NumbersSet], bool]) -> bool:
        valid = True
        index: int = 0

        while (index < self.size) and valid:
            valid = predicate(self.extract_line(index)) and\
                    predicate(self.extract_column(index)) and\
                    predicate(self.extract_zone(index))
            index += 1

        return valid
