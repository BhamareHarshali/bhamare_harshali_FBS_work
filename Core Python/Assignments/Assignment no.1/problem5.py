#5. Write a program to enter P, T, R and calculate Compound Interest.

P = float(input("Enter the pricipal amount :"))
R = float(input("Enter the Rate of interest :"))
T = float(input("Enter the Time in year :"))

A = P * (1 + R/100) ** T   # Total Amount
Compount_Interest = A - P    #CI

#display output
print(f'{Compount_Interest}')  