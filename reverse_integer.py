def reverse_integer(x):
    """
    Reverse digits of an integer.
    
    :param x: Integer to be reversed
    :return: Reversed integer
    """
    sign = -1 if x < 0 else 1  # Determine the sign of the integer
    x *= sign  # Make the integer positive for reversal
    reversed_x = 0  # Initialize the reversed integer

    while x:
        reversed_x = reversed_x * 10 + x % 10  # Add the last digit of x to reversed_x
        x //= 10  # Remove the last digit from x

    reversed_x *= sign  # Restore the original sign

    # Check if the reversed integer is within the 32-bit signed integer range
    if reversed_x < -2**31 or reversed_x > 2**31 - 1:
        return 0  # Return 0 if it is out of range
    return reversed_x

# Example usage
x = 123
print(reverse_integer(x))  # Output should be 321
