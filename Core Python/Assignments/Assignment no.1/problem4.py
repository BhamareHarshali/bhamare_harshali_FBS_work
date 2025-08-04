#4. Write a program to enter P, T, R and calculate simple Interest.

P = float(input("Enter the principal amount :"))
R = float(input("Enter the Rate of interest :"))
T = float(input("Enter the Time in year :"))

Simple_Interest = (P*R*T)/100  #SI Formula SI = (P*R*T)/100

#display output
print(f' {Simple_Interest } . ')