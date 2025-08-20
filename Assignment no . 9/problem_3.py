#3. Write a program to reverse a given number using recursive function.

def reverse(n , rev=0):
    if n == 0:
        return rev
    else:
        return reverse (n // 10 , rev * 10 + n % 10)
    
#Input
num = int(input("Enter a number: "))
rev_num = reverse(num)

# Output
print("Reversed number:", rev_num)    