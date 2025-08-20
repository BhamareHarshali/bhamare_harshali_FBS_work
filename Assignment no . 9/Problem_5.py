#5. Write a program to find factorial using recursion.

def Factorial(n):
    if n == 1:
        return 1
    else:
        return n * Factorial(n-1)
    
num = int(input("Enter the number: "))
fact = Factorial(num) 
print(fact)   