#10. Write a program to reverse three-digit number.

num = int(input("Enter three-digit number : "))

a = num % 10
b = (num // 10) % 10
c = num // 100

reversed = a * 100 + b * 10 + c
print(f'The reversed number is : {reversed}.')