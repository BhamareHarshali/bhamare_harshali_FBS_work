#6. WAP to check if a given number is prime number or not.

num = int(input("Enter number : "))
for i in range (2 ,num // 2):
    print(i)
    if (num % i == 0):
        print(f'{num}: is not a prime number.')
        break
else:
    print(f"{num}: is a prime number. ")    
