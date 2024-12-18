#WAP to get factorial of a number using function

def factorial(num):
    """Calculate the factorial of a number."""
    if num < 0:
        return "Factorial does not exist for negative numbers."
    elif num == 0 or num == 1:
        return 1
    else:
        fact = 1
        for i in range(1, num + 1):
            fact *= i
        return fact

# Input from the user
number = int(input("Enter a number to find its factorial: "))
result = factorial(number)
print(f"The factorial of {number} is {result}")