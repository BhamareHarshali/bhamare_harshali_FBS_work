#12. Write a program to check if given 3 digit number is a palindrome or not.

# Input a 3-digit number from the user
num = int(input("Enter a 3-digit number: "))


# Extract digits
first = num // 100          # First digit
last = num % 10             # Last digit

# Check if first and last digits are the same
if first == last:
        print(f"{num} is a palindrome number")
else:
        print(f"{num} is not a palindrome number")


