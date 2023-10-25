# Input from the user
num = int(input("Enter a number: "))

# Initialize a variable to store the reversed number
reversed_num = 0
while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

# Display the reversed number
print("The reversed number is: ", reversed_num)