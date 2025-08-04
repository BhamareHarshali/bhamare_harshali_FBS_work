#11. Find the area and circumference of circle.

radius = float(input("Enter the radius of the circumference of the circle :"))

#Formula of circle [π = 3,14]
#circumference 2 * π *radius 

pi = 3.14
area = pi * radius * radius # circle area display 
circumference = 2 * pi * radius #circumference area display

#Display output
print(f'Area of the circle is : {area} .')
print(f'Area of the circumference of the circle is : {circumference} .')