#1. Write a program to check if the given number is positive or negative.

num = int(input("Enter the number:"))

if(num < 0):
    print(f'{num}:Negative.')
elif(num >0):
    print(f'{num}:Positive.')
else:
    print(f'{num}:Invalid')        