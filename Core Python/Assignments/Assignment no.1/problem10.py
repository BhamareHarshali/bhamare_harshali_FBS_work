#10. Write a program to calculate area of an equilateral triangle.

side = float(input("Enter the sode of the equilateral triangle : "))

#Formula (√3 /4 * side*side) using [1.732 / 4 * side *side]
area = 1.732 / 4 * side * side

#display output
print(f'Area of the equilateral triangle is : {area} .')