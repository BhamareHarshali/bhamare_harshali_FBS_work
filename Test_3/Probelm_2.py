#2. write a program to calculate the um of following series where n is input by user 
#1/1! + 2/2! + 3/3! + 4/4! + N/N!


num = int(input("Enter the N: "))
total = 0
for i in range(1,num+1):
    total += num ** i  # ** i
print("Sum of the series is:", total)   