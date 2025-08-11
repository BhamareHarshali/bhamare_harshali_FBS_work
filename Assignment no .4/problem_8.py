#8. WAP to find which numbers are divisible by 7 and multiple of 5 in a given range.

a = int(input("Enter the number a: "))
b = int(input("Enter the number b: "))

print("Number is divisible by 7 and multiple of 5 in ")

for i in range ( a ,b+1):
    if(i %7 == 0 and i % 5 == 0):
        print(i)
   