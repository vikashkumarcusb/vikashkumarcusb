def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Input from the user for a list of numbers
arr = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))

# Input from the user for the target element to search
target = int(input("Enter the element you want to search for: "))

# Perform linear search
result = linear_search(arr, target)

# Display the result
if result != -1:
    print(f"{target} found at index {result}")
else:
    print(f"{target} not found in the list.")

