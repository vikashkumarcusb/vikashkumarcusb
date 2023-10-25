def print_numbers(n):
    if n < 0:
        return
    print(n)
    print_numbers(n - 1)

# Input from the user
n = int(input("Enter a number: "))

# Call the recursive function to print numbers from n to 0
print("Numbers from", n, "to 0:")
print_numbers(n)
