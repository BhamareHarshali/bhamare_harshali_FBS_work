#4. Write to check if number is palindrom or not using recursion

def reverse_num(num , rev=0):
    if num == 0:
        return rev
    else:
        return reverse_num(num // 10 ,rev * 10 + num % 10)

def is_palindrome(num):
    return num == reverse_num(num) 

num = int(input("Enter the number: "))
if is_palindrome(num):
    print(f'{num} is a palindrome number.') 
else:      
    print(f'{num} is not a palindrome number.')   