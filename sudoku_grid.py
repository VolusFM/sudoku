from typing import Callable

import numpy as np


def is_set_complete(numbers: list[int]):
    return numbers.count(0) == 0


def is_set_correct(numbers: list[int]) -> bool:
    if not is_set_complete(numbers):
        return False

    i = 0
    while i < len(numbers):
        if numbers.count(i) > 1:
            return False
        i += 1

    return True


class SudokuGrid(object):
    lines: list[list[int]]
    size: int
    zone_size: int

    def __init__(self, lines: list[list[int]]):
        if len(lines) == 0 or len(lines[0]) == 0:
            raise

        self.size = len(lines[0])
        self.zone_size: int = int(np.sqrt(self.size))  # TODO repurpose this to handle non-square grids

        if lines != [line for line in lines if len(line) == self.size]:
            raise

        self.lines = lines

    def extract_line(self, index) -> list[int]:
        return self.lines[index]

    def extract_column(self, index) -> list[int]:
        col: list[int] = []
        for line in self.lines:
            col.append(line[index])

        return col

    def extract_zone(self, index) -> list[int]:
        zone: list[int] = []
        zone_line_index: int = index // self.zone_size
        zone_column_index: int = index % self.zone_size

        for line in range(self.zone_size):
            for column in range(self.zone_size):
                zone.append(self.lines
                            [self.zone_size * zone_line_index + line]
                            [self.zone_size * zone_column_index + column])

        return zone

    def is_complete(self) -> bool:
        return self.apply_predicate_to_grid(is_set_complete)

    def is_correct(self) -> bool:
        return self.apply_predicate_to_grid(is_set_correct)

    def apply_predicate_to_grid(self, predicate: Callable[[list[int]], bool]) -> bool:
        valid = True
        index: int = 0

        while (index < self.size) and valid:
            valid = predicate(self.extract_line(index)) and\
                    predicate(self.extract_column(index)) and\
                    predicate(self.extract_zone(index))
            index += 1

        return valid
