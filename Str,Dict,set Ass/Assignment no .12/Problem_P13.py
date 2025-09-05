#13. Python Program to count number of digits and letters in a string.

str = "Python 123 is fun 2025"

letter = 0
digit = 0

for char in str:
    if char.isalpha():
        letter +=1
    elif char.isdigit():
        digit += 1
        
print("Total Letters :",letter)            
print("Total digit :",digit)            