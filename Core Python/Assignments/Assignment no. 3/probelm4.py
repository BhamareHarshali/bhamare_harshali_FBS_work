#4. Write a program to input all sides of a triangle and check whether triangle is valid or not.

a=int(input("Enter the side 1:"))
b=int(input("Enter the side 2:"))
c=int(input("Enter the side 3:"))

if ((a + b) > c and (b + c) > a and (a + c) > b):
    print("The triangle is valid.")
else:
    print("The triangle is invalid.")    


