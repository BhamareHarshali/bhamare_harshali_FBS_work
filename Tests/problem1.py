#1. Write a program to find the area and perimeter of following figure (Accept the length, breadth and radius from user:

length =float(input("Enter the length of the rectangle :"))
breadth =float(input("Enter the breadth of the rectangle :"))
radius =float(input("Enter the length of the circle :"))

rectangle_area = length * breadth
rectangle_perimeter = 2 * (length + breadth)
total_reactangle = (rectangle_area + rectangle_perimeter)

circle_area = 3.14 * radius * radius
circle_cricumference = 2 * 3.14 * radius
total_circle = (circle_area + circle_cricumference)

print(f'Rectangle (Area + Perimeter): {total_reactangle} , circle (Area + Perimeter): {total_circle} .')