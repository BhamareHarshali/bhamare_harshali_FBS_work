#2. Write a program to check if given number is Armstrong or not using recursive function.

def sum(n ,power):
    if n == 0:
        return 0
    else:
        return (n % 10) ** power + sum(n // 10,power)

def isArmstrong(num):
    digits = len(str(num))              # count digits
    return num == sum(num, digits)    
    
num = int(input("Enter the number: "))
if isArmstrong (num):
    print(f'{num} : is Armstrong number.')

else:
    print(f'{num} : is not Armstrong number.')    