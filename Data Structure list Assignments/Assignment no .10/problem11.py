#11. Write a program to print all numbers which are divisible by m and n in the list.

li =[10,20,30,40,50,60,80,90,100]

m = int(input("Enter value of m: "))
n = int(input("Enter value of n: "))

print(f"Number divisible by {m} and {n}. ")

for i in li:
    if i % m == 0 and i % n == 0:
        print(i)