#6. WAP to calculate total salary of employee based on basic, da=10% of basic,ta=12% of basic, hra=15% of basic.

salary =int(input("Enter the total salary of empolyees : "))

da_amt =salary * 10 /100 
ta_amt = salary * 12 /100 
hra_amt =salary * 15 /100 

total_salary = salary + da_amt + ta_amt + hra_amt

print(f'Total_salary: {total_salary} .')
