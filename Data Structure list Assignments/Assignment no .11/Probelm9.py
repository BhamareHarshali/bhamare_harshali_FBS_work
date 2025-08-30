#9. Write a program to create three lists of numbers, their squares and cubes

n = int(input("Enter the limit : "))

number = []
squares = []
cube = []

for i in range(1,n + 1):
    number.append(i)
    squares.append(i ** 2)
    cube.append(i ** 3)
    
print ("Number : ",number)
print ("Square : ",squares)
print ("Cube : ",cube)    