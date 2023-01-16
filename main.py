from display import SudokuGridDisplayService
from numbers_set import NumbersSet
from sudoku_grid import SudokuGrid
from sudoku_grid_service import SudokuGridService

sudoku_grid_display_service = SudokuGridDisplayService()

# TODO make a helper for creations
test_grid: SudokuGrid = SudokuGrid([NumbersSet(4, [3, 4, 2, 1]),
                                    NumbersSet(4, [1, 2, 4, 3]),
                                    NumbersSet(4, [2, 3, 1, 4]),
                                    NumbersSet(4, [4, 1, 3, 2])])

test_grid_2: SudokuGrid = SudokuGrid([NumbersSet(9, [0, 2, 0, 8, 0, 6, 0, 0, 9]),
                                      NumbersSet(9, [5, 6, 0, 4, 0, 0, 0, 0, 0]),
                                      NumbersSet(9, [9, 0, 7, 5, 0, 0, 0, 8, 4]),
                                      NumbersSet(9, [2, 0, 0, 0, 3, 1, 0, 0, 5]),
                                      NumbersSet(9, [8, 0, 0, 0, 4, 0, 0, 0, 7]),
                                      NumbersSet(9, [7, 0, 0, 9, 8, 0, 0, 0, 1]),
                                      NumbersSet(9, [1, 5, 0, 0, 0, 9, 4, 0, 8]),
                                      NumbersSet(9, [0, 0, 0, 0, 0, 4, 0, 3, 2]),
                                      NumbersSet(9, [4, 0, 0, 2, 0, 8, 0, 9, 0])])

print("GO !")
sudoku_grid_display_service.display_grid(test_grid_2)
sudoku_grid_display_service.display_grid(test_grid)

print(test_grid.extract_line(3).numbers)
print(test_grid.extract_column(3).numbers)
print(test_grid.extract_zone(3).numbers)
print(test_grid.is_complete())
print(test_grid.is_correct())

sgs: SudokuGridService = SudokuGridService()

sudoku_grid_display_service.display_grid(sgs.create_complete_grid(4))
sudoku_grid_display_service.display_grid(sgs.create_complete_grid(9))
