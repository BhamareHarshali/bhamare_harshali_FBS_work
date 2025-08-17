#1. Write a program to calculate area of rectangle

def rectangle(lenght , width):
    return lenght * width

l = float(input("Enter the length of rectangle: "))
w = float(input("Enter the width of rectangle: "))

area = rectangle(l , w)

print("Area of rectangle : ",area)    