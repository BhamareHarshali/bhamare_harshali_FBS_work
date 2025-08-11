#1. WAP to print all even numbers until n.

i  = 1
num = int(input("Enter the number 1 to n : "))
while (i <= num ):
    if num %2 == 0:
       print(i)
    i += 1