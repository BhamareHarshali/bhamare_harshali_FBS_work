#Write a program to accpet basic salary of n emp.
#(n should be accpected from user) . If basic salary is below 20000 then 
#da =10%,ta=12% and hra=15% otherwise da=15% ,ta=18% and hra=20% .
#Based on this calculate the total salary of each emp and also total salary of all emp 

n= int(input("Enter the number of emp: "))
salary =0

for i in range(1,n+1):
    basic = float(input(f'Enter basic salry of emp: {i}: '))
    
    if basic < 2000:
        da = 0.10 * basic
        ta = 0.12 * basic
        hra = 0.15 * basic
    else:
        da = 0.15 * basic    
        ta = 0.18 * basic    
        hra = 0.20 * basic
        
    total_salary = basic + da + ta + hra
    print(f"Total salary of emp {i}:  {salary}: ")
    
    salary +=   total_salary
    print("Salary of emp is :",total_salary)    
