# Program to check if a number is an Armstrong Number

# Step 1: Take input
num = int(input("Enter a number: "))

# Step 2: Calculate number of digits
num_digits = len(str(num))

# Step 3: Calculate sum of powers of digits
temp = num
total = 0
while temp > 0:
    digit = temp % 10
    total += digit ** num_digits
    temp //= 10

# Step 4: Compare and display result
if total == num:
    print(f"{num} is an Armstrong Number")
else:
    print(f"{num} is NOT an Armstrong Number")
