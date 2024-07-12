#include <iostream>
using namespace std;

int main() {
    // Declare variables for number of rows, columns, and the sum of diagonals
    int rows, columns;
    int sum = 0;

    // Prompt user to enter the number of columns
    cout << "Please enter the number of the columns: ";
    cin >> columns;

    // Prompt user to enter the number of rows
    cout << "Please enter the number of the rows: ";
    cin >> rows;

    // Declare a 2D array (matrix) with the specified rows and columns
    int matrix[rows][columns];

    // Loop to get the matrix elements from the user
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < columns; j++) {
            cout << "Please enter A[" << i << "," << j << "]: ";
            cin >> matrix[i][j];
        }
        cout << "\n";
    }

    // Loop to print the matrix elements
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < columns; j++) {
            cout << "A[" << i << "," << j << "]:" << matrix[i][j] << endl;
        }
        cout << "\n";
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
    cout << sum;

    return 0;
}
