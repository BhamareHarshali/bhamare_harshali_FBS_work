#12. Write a program to create three lists of numbers, their squares and cubes

n = int(input("Enter the limit: "))

number = []
squares = []
cubes = []

for i in range(1,n+1):
    number.append(i)
    squares.append(i ** 2)
    cubes.append(i ** 3)
    
print(f'Numbers : {number}') 
print(f'Squares : {squares}')
print(f'Cubes : {cubes}')   