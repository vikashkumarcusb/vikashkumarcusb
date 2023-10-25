# Input from the user for the number of terms in the series
n = int(input("Enter the number of terms you want in the Fibonacci series: "))

# Initialize the first two terms
term1 = 0
term2 = 1

# Check if the user wants to print the series
if n <= 0:
    print("Invalid input. Please enter a positive integer.")
elif n == 1:
    print(f"Fibonacci series with {n} term(s): {term1}")
else:
    print("Fibonacci series:")
    print(term1, term2, end=" ")

    # Generate and print the remaining terms in the series
    for _ in range(2, n):
        next_term = term1 + term2
        print(next_term, end=" ")
        term1, term2 = term2, next_term
    print()

