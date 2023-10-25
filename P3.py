
# Input from the user
num_count = int(input("Enter the number of real numbers you want to multiply: "))

# Initialize the product to 1
product = 1

# real numbers and calculate their product
for i in range(num_count):
    num = float(input(f"Enter real number {i + 1}: "))
    product *= num

# Display the calculated product
print(f"The product of the {num_count} real numbers is: {product}")
