def matrix_diagonal_sum(matrix):
    """
    Calculate the sum of the diagonals of a given matrix.
    
    :param matrix: List of lists, where each inner list represents a row of the matrix
    :return: Sum of the diagonals of the matrix
    """
    rows = len(matrix)  # Number of rows in the matrix
    sum_diagonals = 0   # Initialize sum of diagonals

    for i in range(rows):
        sum_diagonals += matrix[i][i]  # Add the element from the main diagonal
        sum_diagonals += matrix[i][rows - 1 - i]  # Add the element from the anti-diagonal

    if rows % 2 == 1:
        sum_diagonals -= matrix[rows // 2][rows // 2]  # Subtract the middle element if the matrix size is odd

    return sum_diagonals

# Example usage
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix_diagonal_sum(matrix))  # Output should be 25
