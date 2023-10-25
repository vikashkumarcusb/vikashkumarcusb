# Loop through the range 100 to 200 and display numbers with even digit sums

print("Integers within the range 100 to 200 whose sum of digits is even:")

for num in range(100, 201):

    number_str = str(num)

    digit_sum = sum(int(digit) for digit in number_str)
    if digit_sum % 2 == 0:
        print(num)