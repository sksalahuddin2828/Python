# Size of the 2D matrix (N x N)
# grid_size = N / means N = 9
grid_size = 9  

# A utility function to print the grid
def print_grid(grid):
    for row in range(grid_size):
        for col in range(grid_size):
            print(grid[row][col], end=" ")
        print()

# Checks whether it will be legal to assign num to the given row, col
def is_safe(grid, row, col, num):
    # Check if we find the same num in the same row, return False
    for check_col in range(grid_size):
        if grid[row][check_col] == num:
            return False

    # Check if we find the same num in the same column, return False
    for check_row in range(grid_size):
        if grid[check_row][col] == num:
            return False

    # Check if we find the same num in the particular 3x3 matrix, return False
    start_row = row - row % 3
    start_col = col - col % 3
    for check_row in range(3):
        for check_col in range(3):
            if grid[check_row + start_row][check_col + start_col] == num:
                return False
    return True

# Takes a partially filled-in grid and attempts to assign values to all unassigned locations
def solve_sudoku(grid, row, col):
    # Check if we have reached the last row and column, return True to avoid further backtracking
    if row == grid_size - 1 and col == grid_size:
        return True

    # Check if column value becomes grid_size, move to the next row and column start from 0
    if col == grid_size:
        row += 1
        col = 0

    # Check if the current position of the grid already contains a value > 0, iterate for the next column
    if grid[row][col] > 0:
        return solve_sudoku(grid, row, col + 1)

    for num in range(1, grid_size + 1):
        # Check if it is safe to place the num (1-9) in the given row, col
        if is_safe(grid, row, col, num):
            # Assign the num in the current (row, col) position of the grid and assume it is correct
            grid[row][col] = num

            # Check for the next possibility with the next column
            if solve_sudoku(grid, row, col + 1):
                return True

            # If the assumption was wrong, remove the assigned num and go for the next assumption with a different num value
            grid[row][col] = 0

    return False

# Driver Code
# 0 means unassigned cells
grid = [
    [3, 0, 6, 5, 0, 8, 4, 0, 0],
    [5, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 8, 7, 0, 0, 0, 0, 3, 1],
    [0, 0, 3, 0, 1, 0, 0, 8, 0],
    [9, 0, 0, 8, 6, 3, 0, 0, 5],
    [0, 5, 0, 0, 9, 0, 6, 0, 0],
    [1, 3, 0, 0, 0, 0, 2, 5, 0],
    [0, 0, 0, 0, 0, 0, 0, 7, 4],
    [0, 0, 5, 2, 0, 6, 3, 0, 0]
]

if solve_sudoku(grid, 0, 0):
    print_grid(grid)
else:
    print("No solution exists.")

#----------------------------------------------------------------------------------------------------------------------------------------------------------
  
# Answer: 3 1 6 5 7 8 4 9 2 
#         5 2 9 1 3 4 7 6 8 
#         4 8 7 6 2 9 5 3 1 
#         2 6 3 4 1 5 9 8 7 
#         9 7 4 8 6 3 1 2 5 
#         8 5 1 7 9 2 6 4 3 
#         1 3 8 9 4 7 2 5 6 
#         6 9 2 3 5 1 8 7 4 
#         7 4 5 2 8 6 3 1 9 
