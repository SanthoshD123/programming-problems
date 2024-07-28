def print_grid(grid):
    for i in range(9):
        for j in range(9):
            print(grid[i][j], end=" ")
        print()

def is_safe(grid, row, col, num):
    # Check if 'num' is already in the same row or column
    for x in range(9):
        if grid[row][x] == num or grid[x][col] == num:
            return False

    # Check the 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if grid[i][j] == num:
                return False

    return True

def solve_sudoku(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                for num in range(1, 10):
                    if is_safe(grid, row, col, num):
                        grid[row][col] = num
                        if solve_sudoku(grid):
                            return True
                        grid[row][col] = 0
                return False
    return True

# Example usage
if __name__ == "__main__":
    sudoku_grid = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        # ... (fill in the rest of the grid)
    ]

    if solve_sudoku(sudoku_grid):
        print("Solved Sudoku:")
        print_grid(sudoku_grid)
    else:
        print("No solution exists.")
