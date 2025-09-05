#2. Python Program to Remove the nth Index Character from a Non-Empty String

str = "Python"

n = 2
new_str = " "
for i in range(len(str)):
    if i != n:
        new_str += str[i]
        
print("Original String :", str)
print("Modified String :", new_str)                