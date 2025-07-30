#6. Write a Program to input two angles from user and find third angle of the triangle.

angle1 = int(input("Enter the first angle of the triangle: "))
angle2 = int(input("Enter the second angle of the triangle: "))

#180 - (Frist angle + Second angle)  // this is a formula of 3 angle triangle
angle3 = 180 - (angle1 + angle2)

#Display output
print(f'The third angle of the triangle is : {angle3 }')