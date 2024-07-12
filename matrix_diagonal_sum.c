#include <stdio.h>
#include <string.h>

int main() {
    // Variable declarations for number of rows, columns, and sum of diagonals
    int rows, columns;
    int sum = 0;

    // Prompt user for the number of rows
    printf("Please enter the number of the rows: ");
    scanf("%d", &rows);

    // Prompt user for the number of columns
    printf("Please enter the number of the columns: ");
    scanf("%d", &columns);

    // Declare a 2D array (matrix) with the specified rows and columns
    int matrix[rows][columns];

    // Loop to get the matrix elements from the user
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < columns; j++) {
            printf("Please enter Array[%d][%d]: ", i, j);
            scanf("%d", &matrix[i][j]);
        }
        printf("\n");
    }

    printf("\n");

    // Loop to print the matrix elements
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < columns; j++) {
            printf("Array[%d][%d] = %d", i, j, matrix[i][j]);
            printf("\n");
        }
        printf("\n");
    }

    // Loop to calculate the sum of the diagonals
    for (int i = 0; i < rows; i++) {
        sum += matrix[i][i] + matrix[i][rows - 1 - i];
    }

    // Adjust sum if the matrix has an odd number of rows (subtract the middle element)
    if (rows % 2 == 1) {
        sum -= matrix[rows / 2][rows / 2];
    }

    // Print the sum of the diagonals
    printf("Sum of diagonals: %d\n", sum);

    return 0;
}
