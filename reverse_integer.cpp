#include <iostream>
#include <math.h>
using namespace std;

int main() {
    // Declare a double variable 'r' to store the value 2^31
    double r = pow(2, 31);

    // Declare integer variables 'number' and 'digit'
    int number;
    int digit;

    // Prompt the user to enter a number
    cout << "Please enter a number: ";
    cin >> number;

    // Check if the number is within the range of -2^31 to 2^31
    if (number <= r && number >= -r) {
        // If the number is negative, print the minus sign and make the number positive
        if (number < 0) {
            number *= -1;
            cout << "-";
        }

        // Loop to extract and print each digit of the number in reverse order
        while (number > 0) {
            digit = number % 10;  // Get the last digit of the number
            number = number / 10; // Remove the last digit from the number
            cout << digit;        // Print the digit
        }
    }

    return 0;
}
