#10.Python Program to Take in Two Strings and Display the Larger String without Using Built-in Functions

str1 = "Python Programming"
str2 = "Programming"

len1 = 0
for char in str1:
    len1 += 1
    
len2 = 0  
for char in str2:
    len2 += 1
    
if len1 > len2:
    print("Largest String is :",str1) 
    
elif len2 > len1:
    print("Largest String is :",str2) 
        
else:
    print("Both String are equal length")            