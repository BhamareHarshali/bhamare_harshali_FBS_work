# 2. Write a program to calculate area of circle

def circle(radius):
    
    return 3.14 * radius * radius

r =float(input("Enter the radius of circle : "))

area = circle(r)

print("Area of circle: ",area)