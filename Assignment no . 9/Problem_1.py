#1. Write a program to find sum of following series using recursive functions:
#i. 1! + 2! + 3! + 4! +..... + n!
#Note : For fact and sum two recursive functions

def Factorial(n):
    if n == 1:
        return 1
    else:
        return (n * Factorial (n -1))

def SOS(n):
    if n== 0:
        return 0 
    else:
        return Factorial(n) + ( SOS(n-1))
        
num = int(input("Enter the number: "))
res = SOS(num)
print("Sum of series (1! + 2! + ... +", num, "!) =", res)

