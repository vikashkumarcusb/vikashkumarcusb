def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid  # Return the index if the target is found
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Return -1 if the target is not found


# Input from the user for a sorted list of numbers
arr = sorted(list(map(int, input("Enter a sorted list of numbers separated by spaces: ").split())))

# Input from the user for the target element to search
target = int(input("Enter the element you want to search for: "))

# Perform binary search
result = binary_search(arr, target)

# Display the result
if result != -1:
    print(f"{target} found at index {result}")
else:
    print(f"{target} not found in the list.")
