#4. Write a program to find sum of n numbers using recursion.

def SON(n):
    if n == 0:
        return 0
    else:
        return (n + SON (n-1))
num = int(input("Enter the number: "))
sum = SON(num)
print(sum)    