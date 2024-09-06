def is_armstrong_number(number):
    # Convert the number to a string to easily iterate over digits
    num_str = str(number)
    # Get the number of digits
    num_digits = len(num_str)
    # Calculate the sum of each digit raised to the power of num_digits
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    # Check if the sum of powers is equal to the original number
    return sum_of_powers == number

# Input: get number from user
try:
    num = int(input("Enter a number: "))
    if is_armstrong_number(num):
        print(f"{num} is an Armstrong number.")
    else:
        print(f"{num} is not an Armstrong number.")
except ValueError:
    print("Invalid input. Please enter a valid integer.")
