#7. Program to Find the Roots of a Quadratic Equation

a = float(input("Enter the value : "))
b = float(input("Enter the value : "))
c = float(input("Enter the value : "))

sqrt = ((b ** 2)-(4 *a * c)) ** 0.5
ans1 = (-b+sqrt)/2*a
ans2 = (-b - sqrt)/2*a

print(f'Roots of a Quadratic Equation is :{ans1} and {ans2} ')
