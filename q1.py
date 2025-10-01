def swap(x, y):
    """
    Task 1
    - Create a function that would swap the value of x and y using only x and y as variables.
    - x and y must be numeric.
    - Return -1 if x and y is not numeric, and
    - print the swapped values if both x and y are numeric.
    """
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        return -1

    # Swap using arithmetic (no third variable)
    x = x + y
    y = x - y
    x = x - y

    print("Swapped values: x =", x, ", y =", y)

# Task 2 – Invoke the function:

# Case 1: Non-numeric input
result1 = swap("Apple", 10)
print("Result:", result1)  # Expected output: -1

# Case 2: Numeric input
result2 = swap(9, 17)
# Expected print: Swapped values: x = 17 , y = 9

print("Result:", result2)  # Expected output: None (since function only prints)
