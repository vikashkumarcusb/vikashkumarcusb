import math

# Input from the user
num = int(input("Enter an integer: "))

# Check if the number is prime
is_prime = True

# For special cases (0, 1, and negative numbers)
if num <= 1:
    is_prime = False
else:
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            is_prime = False
            break

# Display the result
if is_prime:
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")


