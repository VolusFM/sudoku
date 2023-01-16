from __future__ import annotations


class NumbersSet(object):
    numbers: list[int]
    size: int

    def __init__(self, size: int, numbers: list[int]):
        if len(numbers) != size:
            raise
        self.numbers = numbers
        self.size = size

    def extract_filled_numbers(self) -> NumbersSet:
        extracted_numbers: list[int] = [number for number in self.numbers if number > 0]

        return NumbersSet(len(extracted_numbers), extracted_numbers)

    def is_complete(self) -> bool:
        return self.numbers.count(0) == 0

    def is_correct(self) -> bool:
        if not self.is_complete():
            return False

        i = 0
        while i < len(self.numbers):
            if self.numbers.count(i) > 1:
                return False
            i += 1

        return True
