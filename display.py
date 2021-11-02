import os


def display(grid):
    ans = f'{os.linesep}+-------+-------+-------+{os.linesep}'
    for line in range(9):
        ans = f'{ans}| '
        for column in range(9):
            number_string = "_" if grid[line][column] == 0 else grid[line][column]
            ans = f'{ans}{number_string} '
            if (column + 1) % 3 == 0:
                ans = f'{ans}| '
            if ((line + 1) % 3 == 0) and (line < 6) and (column == 8):
                ans = f'{ans}{os.linesep}|-------+-------+-------|'
        ans = f'{ans}{os.linesep}'
    ans = f'{ans}+-------+-------+-------+'
    print(ans)
