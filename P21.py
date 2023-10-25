
# Input from the user for the list of numbers
numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))

# Input from the user for the number to insert
number_to_insert = int(input("Enter the number to insert: "))

# Input from the user for the position to insert the number
position = int(input(f"Enter the position (0 to {len(numbers)}) to insert the number: "))

# Check if the position is within a valid range
if position < 0 or position > len(numbers):
    print("Invalid position. The position should be between 0 and", len(numbers))
else:
    # Insert the number at the specified position
    numbers.insert(position, number_to_insert)

    # Display the updated list
    print("Updated list:", numbers)

