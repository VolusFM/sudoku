class NumbersSet(object):
    def __init__(self, numbers):
        if len(numbers) != 9:
            raise
        self.numbers = numbers

    def is_complete(self):
        return self.numbers.count(0) != 0

    def is_correct(self):
        i = 0
        while i < len(self.numbers):
            if self.numbers(self.numbers[i]) > 1:
                return False
            i += 1

        return True
