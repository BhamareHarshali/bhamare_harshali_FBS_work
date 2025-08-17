#11. WAP to check if a given number is Armstrong number or not. For each task create separate functions.

def is_armstrong(num):
    # count digits
    n = len(str(num))
    total = 0
    temp = num

    while temp > 0:
        digit = temp % 10
        total += digit ** n   # raise digit to power of number of digits
        temp //= 10

    return total == num


# --- Main program ---
num = int(input("Enter a number: "))

if is_armstrong(num):
    print(num, "is an Armstrong number.")
else:
    print(num, "is NOT an Armstrong number.")
