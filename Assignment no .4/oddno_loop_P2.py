#2. WAP to print all odd numbers until n.

i = 1
num = int(input("Enter the number up to n: "))

while (i <= num):
    if (i %2 != 0):
        print(i)
    i += 1        