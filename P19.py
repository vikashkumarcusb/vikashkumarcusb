# Input from the user for the array
array = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))

# Find and collect odd numbers
odd_numbers = [num for num in array if num % 2 != 0]

# Display the odd numbers
print("Odd numbers in the array:", odd_numbers)
