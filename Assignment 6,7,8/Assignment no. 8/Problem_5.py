#5. Sum of all prime numbers between 1 to n

def CheckPrime(num):
    if num < 2:   # 0 and 1 are not prime
        return False
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False
    return True

def SumPrime(n):
    total = 0
    for i in range(1, n+1):
        if CheckPrime(i):
            total += i
    return total

# Input
n = int(input("Enter number: "))

print(f"Sum of all prime numbers between 1 and {n} = {SumPrime(n)}")

