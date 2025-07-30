#8. Write a program to convert days into years, weeks and days.

#Input form user
Days = int(input("Enter the days: "))

Years = Days // 365
#Calculates Day, Weeks , year 
Days = Days // 7
Weeks = Days // 7
Days = Days % 7 

#Display output
print(f'{Years}years {Weeks}weeks {Days}days .')