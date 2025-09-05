#12. Python Program to count number of lowercase characters in a string.

str = "PYTHON Programming is Fun."

count = 0

for char in str:
    if char.islower():
        count += 1
        
print("Total LowerCase Characters: ",count)        
