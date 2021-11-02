import os


def display(grid):
    ans = os.linesep + "+-------+-------+-------+" + os.linesep
    for i in range(9):
        ans += "| "
        for j in range(9):
            ans += str(grid[i][j]) + " "
            if (j + 1) % 3 == 0:
                ans += "| "
            if ((i + 1) % 3 == 0) and (i < 6) and (j == 8):
                ans += os.linesep + "|-------+-------+-------|"
        ans += os.linesep
    ans += "+-------+-------+-------+"
    print(ans)
