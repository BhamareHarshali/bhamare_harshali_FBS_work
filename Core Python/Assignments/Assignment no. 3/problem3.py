#3. Write a program to input angles of a triangle and check whether triangle is valid or not.

angle1 =int(input("Enter angle 1 is :"))
angle2 =int(input("Enter angle 2 is :"))
angle3 =int(input("Enter angle 3 is :"))

if(angle1 + angle2 + angle3 == 180):
    print("Triangle is valid.")
else:
    print("Triangle is invalid.")     
