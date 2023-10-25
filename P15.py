def factorial(n):
    if n == 0:
        return 1  # factorial of 0 is 1
    else:
        return n * factorial(n - 1)

# Input from the user
n = int(input("Enter a non-negative integer: "))

if n < 0:
    print("Factorial is not defined for negative numbers.")
else:
    result = factorial(n)
    print(f"The factorial of {n} is {result}")

