def sum_three_numbers(a, b, c):
    """
    Returns the sum of three numbers.
    
    Args:
        a (int): The first number.
        b (int): The second number.
        c (int): The third number.
    
    Returns:
        int: The sum of a, b, and c.
    """
    return a + b + c

# Example usage:
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

result = sum_three_numbers(num1, num2, num3)
print("The sum is:", result)
