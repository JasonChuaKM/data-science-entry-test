def check_divisibility(num, divisor):
    """
    Task 1
    - Create a function to check if the number (num) is divisible by another number (divisor).
    - Both num and divisor must be numeric.
    - Return True if num is divisible by divisor, False otherwise.
    """
    return

def check_divisibility(num, divisor):
    
    # Step 1: Check if both inputs are numbers (int or float).
    # If either is not numeric, return False immediately.
    if not (isinstance(num, (int, float)) and isinstance(divisor, (int, float))):
        return False
    
    # Step 2: Prevent division by zero.
    # If divisor is zero, divisibility cannot be checked.
    if divisor == 0:
        return False

    # Step 3: Use modulo operator (%) to check divisibility.
    # If the remainder of num / divisor is zero, it is divisible.
    return num % divisor == 0


# Task 2: Test the function with given scenarios
print(check_divisibility(10, 2))  # True because 10 is divisible by 2
print(check_divisibility(7, 3))   # False because 7 is not divisible by 3


# Task 2
# Invoke the function "check_divisibility" using the following scenarios:
# - 10, 2
# - 7, 3
