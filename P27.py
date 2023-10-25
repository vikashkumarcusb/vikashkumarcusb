
def fibonacci(n):
    if n <= 0:
        return "Invalid input"  # Fibonacci series is defined for positive integers
    elif n == 1:
        return 0  # The first term of the series
    elif n == 2:
        return 1  # The second term of the series
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Input from the user for the term number
n = int(input("Enter the term number (N) in the Fibonacci series: "))

# Calculate and display the Nth term
result = fibonacci(n)
if result == "Invalid input":
    print(result)
else:
    print(f"The {n}th term in the Fibonacci series is: {result}")
