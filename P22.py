# Input from the user for the list of elements
elements = input("Enter a list of elements separated by spaces: ").split()

# Convert elements to a list of integers
numbers = [int(element) for element in elements]

# Input from the user for the index to delete
index_to_delete = int(input(f"Enter the index (0 to {len(numbers) - 1}) to delete: "))

# Check if the index is within a valid range
if index_to_delete < 0 or index_to_delete >= len(numbers):
    print(f"Invalid index. The index should be between 0 and {len(numbers) - 1}.")
else:
    # Delete the element at the specified index
    del numbers[index_to_delete]

    # Display the updated list
    print("Updated list:", numbers)


