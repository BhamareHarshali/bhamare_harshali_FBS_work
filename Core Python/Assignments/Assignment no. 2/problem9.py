#9. Write a program to swap two numbers without using third variable.

x = int(input("Enter the number 1: "))
y = int(input("Enter the number 2: "))

x,y = y,x

print(f'X:{x} , Y:{y} .')