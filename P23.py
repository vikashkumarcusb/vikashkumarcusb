# Input from the user
string = input("Enter a string: ")

# Remove spaces and convert to lowercase for case-insensitive comparison
cleaned_string = string.replace(" ", "").lower()

# Check if the cleaned string is equal to its reverse
if cleaned_string == cleaned_string[::-1]:
    print("The entered string is a palindrome.")
else:
    print("The entered string is not a palindrome.")




