#7. Write a program to find sum of digits of a number.

def sum_of_digit(num):
    total = 0 
    while num > 0:
        digit = num % 10
        total += digit
        num //= 10
    return total 

n = int(input("Enter the number: "))

print("Sum of digit: ",sum_of_digit(n))