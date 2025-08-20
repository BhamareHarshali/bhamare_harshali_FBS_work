#6. Write a program to print Fibonacci series using recursion.

def Fibo(n , a, b):
    if n > 0:
        c = a + b
        print(c)
        Fibo(n-1,b,c)
        
num = int(input("Enter the number: ")) 
a = -1
b =1
Fibo(num , a,b)       
        