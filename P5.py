# Input from the user
num = int(input("Enter an integer: "))

# Check if the number is a multiple of both 5 and 7
if num % 5 == 0 and num % 7 == 0:
    print(f"{num} is a multiple of both 5 and 7.")
else:
    print(f"{num} is not a multiple of both 5 and 7.")

