
# Input from the user
N = int(input("Enter the upper limit N: "))

# Initialize a list to store prime numbers
prime_numbers = []

# Loop through the range from 2 to N
for num in range(2, N + 1):
    is_prime = True
    # Check if num is prime
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        prime_numbers.append(num)

# Display the list of prime numbers
print("Prime numbers from 1 to", N, "are:")
print(prime_numbers)