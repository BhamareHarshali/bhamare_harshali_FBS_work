#8. Write a program to check whether a number is prime or not using recursion.

def CheckPrime(n ,i=2):
    if n <= 1:
        return False
    if i == n:
        return True
    if n % i == 0:
        return False
    return CheckPrime(n ,i+1)
    
num = int(input("Enter the number: "))

if CheckPrime(num):
    print(f'{num} is a prime number. ')
else:
    print(f'{num} is not a prime number. ')
    

    
        