#5. Python Program to Count the Number of Vowels in a String

str = "Index"
count = 0
vowels = "aeiouAEIOU"

for char in str:
    if char in vowels:
        print(char ,end='')
        count += 1
        
print("String :",vowels)
print("total count :",count)        
        