#1. Write a program to accept year from user and check if it is a leap year or not.

year = int(input("Enter the year : "))

if (year % 4 != 0):
    print("Not a leap year. ")
elif(year % 100 != 0 ): 
    print("Leap yaer") 
elif(year % 400 == 0):
    print("leap year")     
else:
    print("Not a leap year.")
     