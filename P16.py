# Input from the user for the number of values
n = int(input("Enter the number of values you want to sum: "))

# Initialize an empty list to store the values
values = []

# Input from the user for each value and add them to the list
for i in range(n):
    value = float(input(f"Enter value {i + 1}: "))
    values.append(value)

# Calculate the sum of the values using the built-in sum() function
total = sum(values)

# Display the sum of the values
print(f"The sum of {n} values is: {total}")
