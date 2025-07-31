#2. Write a program to calculate simple interest based on Principal, Rate and Time(SI = P*R*T/100)

P = int(input("Enter the Principal amount :"))
R = int(input("Enter the Rate of interest :"))
T = int(input("Enter the time in year : "))

SI = (P*R*T)/100

print(f'Simple_Interest : {SI} .')