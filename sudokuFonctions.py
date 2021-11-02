# -*- coding: utf-8 -*-
"""
@author: François Montigny
@version : 0.3.0
"""

from random import randrange


def extract_line(line, grid):
    ans = []
    for column in range(9):
        if grid[line][column] != 0:
            ans.append(grid[line][column])
    return ans


def extract_column(column, grid):
    ans = []
    for line in range(9):
        if grid[line][column] != 0:
            ans.append(grid[line][column])
    return ans


def extract_zone(zone, grid):
    ans = []
    line_number = zone // 3
    column_number = zone % 3
    for i in range(3):
        for j in range(3):
            if grid[3 * line_number + i][3 * column_number + j] != 0:
                ans.append(grid[3 * line_number + i][3 * column_number + j])
    return ans


def search(sequence, element):
    i = 0
    while (i < 9) and (sequence[i] != element):
        i += 1
    if i != 9:
        return i
    return -1


def check_ens(ens):
    i = 0
    while i < len(ens):
        if ens.count(ens[i]) > 1:
            return False
        i += 1

    return True


def check_line(line, grille):
    return check_ens(extract_line(line, grille))


def check_column(column, grille):
    return check_ens(extract_column(column, grille))


def check_zone(zone, grille):
    return check_ens(extract_zone(zone, grille))


def check_grid(grille):
    valid = True
    k = 0
    while (k < 9) and (valid is not False):
        valid = check_ens(extract_line(k, grille)) and check_ens(extract_column(k, grille)) \
                and check_ens(extract_zone(k, grille))
        k += 1
    return valid


def create_full_grid():
    grid = [[0 for j in range(9)] for i in range(9)]

    for i in range(9):
        for j in range(9):
            possible_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            for deltaI in range(0, i):
                for deltaJ in range(0, j):
                    if grid[i - deltaI][j - deltaJ] in possible_numbers:
                        print(grid[i - deltaI][j - deltaJ])
                        print(possible_numbers)
                        possible_numbers.remove(grid[i - deltaI][j - deltaJ])
            if len(possible_numbers) != 0:
                index = randrange(0, len(possible_numbers), 1)
                grid[i][j] = possible_numbers[index]

    return grid


# On fera ensuite du "digging" (enlever des nombres) sur la grille. À chaque nombre retiré, on résout la grille.
# S'il y a plusieur solutions, on remet le nombre enlevé. Sinon, on l'enlève. Puis on continue.


def init_backtracking(grid):
    non_prefilled_cells = 0
    indexes = []
    for line in range(9):
        for column in range(9):
            if grid[line][column] == 0:
                non_prefilled_cells += 1
                indexes.append((line, column))
    return non_prefilled_cells, indexes


def backtracking(grille):
    nbCasesNonPreremplies, indices = init_backtracking(grille)

    ans = list(grille)
    p = 0
    nbCasesCompletees = 0

    while (nbCasesCompletees != nbCasesNonPreremplies):
        i = indices[p][0]
        j = indices[p][1]
        ans[i][j] = 1

        while (ans[i][j] <= 9) and ((check_line(i, ans) == 0) or (check_column(j, ans) == 0)):
            if (check_line(i, ans) == 0) or (check_column(j, ans) == 0):
                ans[i][j] = 1

        if (ans[i][j] == 10):
            ans[i][j] = 0
            nbCasesCompletees -= 1
            p -= 1
        else:v
            nbCasesCompletees += 1
            p += 1

    if (nbCasesCompletees == nbCasesNonPreremplies):
        return ans
    else:
        return "Grille insoluble par backtracking."


def afficherGrille(grille):
    ans = "\n--- Grille de Sudoku ----\n+-------+-------+-------+\n"
    for i in range(9):
        ans += "| "
        for j in range(9):
            ans += str(grille[i][j]) + " "
            if ((j + 1) % 3 == 0):
                ans += "| "
            if ((i + 1) % 3 == 0 and i < 6 and j == 8):
                ans += "\n|-------+-------+-------|"
        ans += "\n"
    ans += "+-------+-------+-------+"
    print(ans)


# grille = creerGrilleRemplie()

grilleTest = [[0, 2, 0, 8, 0, 6, 0, 0, 9], [5, 6, 0, 4, 0, 0, 0, 0, 0], [9, 0, 7, 5, 0, 0, 0, 8, 4],
              [2, 0, 0, 0, 3, 1, 0, 0, 5], [8, 0, 0, 0, 4, 0, 0, 0, 7], [7, 0, 0, 9, 8, 0, 0, 0, 1],
              [1, 5, 0, 0, 0, 9, 4, 0, 8], [0, 0, 0, 0, 0, 4, 0, 3, 2], [4, 0, 0, 2, 0, 8, 0, 9, 0]]
print("GO !")
print(afficherGrille(grilleTest))
grilleRemplie = backtracking(grilleTest)
print(afficherGrille(grilleRemplie))
