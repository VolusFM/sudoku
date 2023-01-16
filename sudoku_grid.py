from typing import Callable

import numpy as np

from numbers_set import NumbersSet


class SudokuGrid(list[NumbersSet]):
    zone_size: int
    size: int

    def __init__(self, lines: list[list[int]]):
        if len(lines) == 0 or len(lines[0]) == 0:
            raise

        self.size = len(lines[0])
        self.zone_size: int = int(np.sqrt(self.size))  # TODO repurpose this to handle non-square grids

        if lines != [line for line in lines if len(line) == self.size]:
            raise

        super().__init__(lines)

    def __getitem__(self, index) -> NumbersSet:
        return NumbersSet(self.size, super().__getitem__(index))

    def __setitem__(self, key, value) -> None:
        super().__setitem__(key, value)

    def extract_column(self, index) -> NumbersSet:
        col: list[int] = []
        for line in self:
            col.append(line[index])

        return NumbersSet(self.size, col)

    def extract_zone(self, index) -> NumbersSet:
        zone: list[int] = []
        zone_line_index: int = index // self.zone_size
        zone_column_index: int = index % self.zone_size

        for line in range(self.zone_size):
            for column in range(self.zone_size):
                zone.append(self
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
            valid = predicate(self.__getitem__(index)) and\
                    predicate(self.extract_column(index)) and\
                    predicate(self.extract_zone(index))
            index += 1

        return valid
