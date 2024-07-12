def is_valid(board, row, col, num):
    """
    Check if it's valid to place the number 'num' in the given cell.
    
    :param board: 2D list representing the Sudoku board
    :param row: Row index
    :param col: Column index
    :param num: Number to be placed
    :return: True if it's valid, False otherwise
    """
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False  # Check row and column

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False  # Check 3x3 sub-box
    return True

def solve_sudoku(board):
    """
    Solve the Sudoku puzzle using backtracking.
    
    :param board: 2D list representing the Sudoku board
    :return: True if the Sudoku is solved, False otherwise
    """
    for row in range(9):
        for col in range(9):
            if board[row][col] == '.':
                for num in '123456789':
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True  # Recur to solve the next cell
                        board[row][col] = '.'  # Undo the move (backtrack)
                return False
    return True

# Example usage
sudoku_board = [
    ['5', '3', '.', '.', '7', '.', '.', '.', '.'],
    ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
    ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
    ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
    ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
    ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
    ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
    ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
    ['.', '.', '.', '.', '8', '.', '.', '7', '9']
]

if solve_sudoku(sudoku_board):
    for row in sudoku_board:
        print(" ".join(row))
else:
    print("No solution exists")
