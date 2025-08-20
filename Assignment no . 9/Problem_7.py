#7. Write a program to find sum of digits using recursion.

def SOD(n):
    if n == 0:
        return 0
    else:
        return (n % 10) + SOD (n // 10)
    
num = int(input("Enter the number: "))
print("Sum of digit",SOD(num))    