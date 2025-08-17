#9. Write a program to check if entered number is a palindrome or not.

# 9. Check if number is Palindrome

def is_palindrome(num):
    temp = num
    rev = 0
    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num //= 10
    return temp == rev   # True if palindrome

# Input
n = int(input("Enter a number: "))

if is_palindrome(n):
    print(f"{n} is a Palindrome number.")
else:
    print(f"{n} is NOT a Palindrome number.")
