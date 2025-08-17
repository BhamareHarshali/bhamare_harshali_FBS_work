#3. Write a program to find sum of following series using functions :
#a. 1+ 2 + 3 + 4+..... + n
#b. 1!+ 2! + 3! + 4!+..... + n!
#c. 1^1 + 2^2 + 3^3+ ...... n^n

# Function to calculate factorial of a number
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact  

# a. Sum of natural numbers 1 + 2 + ... + n
def sum_natural(n):
    return n * (n + 1) // 2

# b. Sum of factorials 1! + 2! + ... + n!
def sum_factorial(n):
    total = 0
    for i in range(1, n + 1):
        total += factorial(i)   # FIXED: use factorial function
    return total   

# c. Sum of powers 1^1 + 2^2 + ... + n^n
def sum_power(n):
    total = 0
    for i in range(1, n + 1):
        total += i ** i
    return total

# ----------- MAIN PROGRAM -----------
n = int(input("Enter the value of n: "))

print("1. Sum of natural numbers:", sum_natural(n)) 
print("2. Sum of factorials:", sum_factorial(n))
print("3. Sum of powers:", sum_power(n))

         