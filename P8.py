# Input from the user
num = int(input("Enter an integer: "))

# Initialize a variable to store the sum of the digits
SumOfDigits = 0

# Use a while loop to extract and sum the digits
while num > 0:

    LastDigit = num % 10

    SumOfDigits += LastDigit

    num = num // 10

# Display the sum of the digits
print(f"The sum of the digits is: {SumOfDigits}")

