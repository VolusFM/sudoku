class NumbersSet(list[int]):
    size: int

    def __init__(self, size: int, numbers: list[int]):
        if len(numbers) != size:
            raise
        super().__init__(int(number) for number in numbers)
        self.size = size

    # TODO https://stackoverflow.com/questions/1957780/how-to-override-the-operator-in-python
    # https://realpython.com/inherit-python-list/#creating-list-like-classes-in-python

    def __getitem__(self, item) -> int:
        return super.__getitem__(self, item)

    def __setitem__(self, key, value) -> None:
        super.__setitem__(self, key, value)

    def is_complete(self) -> bool:
        return self.count(0) == 0

    def is_correct(self):
        i = 0
        while i < len(self):
            if self.count(i) > 1:
                return False
            i += 1

        return True
