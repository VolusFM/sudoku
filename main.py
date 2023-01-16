from display import SudokuGridDisplayService
from sudoku_grid import SudokuGrid

sudoku_grid_display_service = SudokuGridDisplayService()

test_grid: SudokuGrid = SudokuGrid([[3, 4, 2, 1],
                                    [1, 2, 4, 3],
                                    [2, 3, 1, 4],
                                    [4, 1, 3, 2]])

test_grid_2: SudokuGrid = SudokuGrid(
    [[0, 2, 0, 8, 0, 6, 0, 0, 9], [5, 6, 0, 4, 0, 0, 0, 0, 0], [9, 0, 7, 5, 0, 0, 0, 8, 4],
     [2, 0, 0, 0, 3, 1, 0, 0, 5], [8, 0, 0, 0, 4, 0, 0, 0, 7], [7, 0, 0, 9, 8, 0, 0, 0, 1],
     [1, 5, 0, 0, 0, 9, 4, 0, 8], [0, 0, 0, 0, 0, 4, 0, 3, 2], [4, 0, 0, 2, 0, 8, 0, 9, 0]])

print("GO !")
sudoku_grid_display_service.display_grid(test_grid_2)
sudoku_grid_display_service.display_grid(test_grid)

print(test_grid[3])
print(test_grid.extract_column(3))
print(test_grid.extract_zone(3))
print(test_grid.is_complete())
print(test_grid.is_correct())
