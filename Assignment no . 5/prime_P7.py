#7. Write a program to print first n prime numbers.

n= int(input("Enter frist n prime number: "))
count = 0
num = 2

while count < n:
    for i in range(2,num):
        if  num % i == 0:
            break


    else:
        print(num) 
        count += 1
    num +=1        
    