#4. WAP to print factorial of a number .
num = int(input("Enter number: "))
fact = 1

for i in range (1,num +1):
    fact = fact  * i
print(f"Factorial of {num}:{fact}")            