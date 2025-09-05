#15. Python Program to find larger string without using built-in functions.

str1 = "Python"
str2 = "Programming"

len1 = 0
for char in str1:
    len1 += 1

len2 = 0
for char in str2:
    len2 += 2
    
if len1 > len2:
    print("Largest String is :",str1)   
elif len2 > len1:     
    print("Largest String is :",str2) 
else:       
    print("Both String are equal in length :")    
    