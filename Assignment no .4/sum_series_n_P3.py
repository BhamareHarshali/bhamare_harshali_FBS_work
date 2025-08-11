#3. WAP to print sum of series upto n.
'''
#using while loop 
num = int(input("Enter the number upto n :"))
sum = 0
i = 1
while i <= num:
    sum +=i
    i += 1
print(f"Sum of series up to n {num} : {sum}.")             
'''

#for using for loop
num = int(input('Enter the number upto n :'))

sum = 0

for i in range (1 , num + 1):
    sum += i
print(f"Sum of series up to n {num} : {sum}.")     