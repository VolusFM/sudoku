class Grid(object):
    def __init__(self, lines):
        if len(lines) != 9:
            raise
        self.lines = lines

    def extract_line(self, number):
        return self.lines[number]

    def extract_column(self, number):
        ans = []
        for line in self.lines:
            ans.append(self.lines[line][number])

        return ans

    def extract_zone(self, number):
        ans = []
        line_number = number // 3
        column_number = number % 3
        for line in range(3):
            for column in range(3):
                if self.lines[3 * line_number + line][3 * column_number + column] != 0:
                    ans.append(self.lines[3 * line_number + line][3 * column_number + column])

        return ans
