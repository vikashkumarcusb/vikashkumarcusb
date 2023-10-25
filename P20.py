
# Input from the user
numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))

# Initialize a variable to store the maximum number
maximum = numbers[0]

# Iterate through the list to find the maximum number
for num in numbers:
    if num > maximum:
        maximum = num

# Display the maximum number
print("The largest number in the list is:", maximum)
